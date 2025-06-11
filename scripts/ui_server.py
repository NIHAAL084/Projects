from pathlib import Path
import gradio as gr
import pandas as pd
import plotly.express as px
import datetime
import base64
import requests
import io
from pymongo import MongoClient
import hashlib



# MongoDB setup
client = MongoClient("mongodb://nihaal:root@localhost:27017/")
db = client["Converstion_Memory"]
cache_col = db["response_caching"]
log_col = db["chat_logs"]

# For analytics
query_log = []
session_id = str(datetime.datetime.now().strftime("session-%Y%m%d-%H%M%S"))
# Constants for the webhook URL

WEBHOOK_URL = "http://localhost:5678/webhook-test/ask-faq"


MAX_CACHE_SIZE = 50

def maintain_cache_size():
    total = cache_col.count_documents({})
    if total > MAX_CACHE_SIZE:
        # Sort by timestamp, remove oldest
        excess = total - MAX_CACHE_SIZE
        old_entries = cache_col.find().sort("timestamp", 1).limit(excess)
        ids_to_delete = [doc["_id"] for doc in old_entries]
        if ids_to_delete:
            cache_col.delete_many({"_id": {"$in": ids_to_delete}})


def encode_file_to_base64(file):
    if file is None:
        return ""
    # If file is already bytes, just encode it
    return base64.b64encode(file).decode('utf-8')


def chroma_interface(query, image_file, table_file):
    image_base64 = encode_file_to_base64(image_file)

    table_csv = ""
    if table_file is not None:
        table_csv = table_file.decode("utf-8")  # file is already bytes

    payload = {
        "query": query,
        "image_base64": image_base64,
        "table_csv": table_csv,
        "sessionId": session_id
    }

    # --- Generate a simple cache key using query hash only ---
    cache_key = hashlib.sha256(query.encode("utf-8")).hexdigest()

    # --- Check cache ---
    cached = cache_col.find_one({"cache_key": cache_key})
    if cached:
        answer = cached["answer"]
        print("✅ Served from cache")
    else:
        try:
            response = requests.post(WEBHOOK_URL, json=payload)
            response.raise_for_status()
            result = response.json()
            answer = result[0].get("answer", "No answer returned.")

            # Save to cache
            cache_col.insert_one({
                "cache_key": cache_key,
                "query": query,
                "answer": answer,
                "timestamp": datetime.datetime.now()
            })
            maintain_cache_size()

        except requests.exceptions.RequestException as e:
            return f"Error during request: {e}"

    # Save to local session log
    query_log.append({
        "timestamp": datetime.datetime.now(),
        "query": query,
        "session": session_id,
        "answer_length": len(answer.split()),
        "used_image": image_file is not None,
        "used_table": table_file is not None,
        "is_fallback": "I’m sorry, but I don’t have enough information" in answer
    })

    # Also persist full interaction to MongoDB logs
    log_col.insert_one({
        "timestamp": datetime.datetime.now(),
        "session": session_id,
        "query": query,
        "answer": answer,
        "image_uploaded": image_file is not None,
        "table_uploaded": table_file is not None
    })

    return answer



def show_analytics():
    # Local Session Data
    session_df = pd.DataFrame(query_log)
    global_df = pd.DataFrame(log_col.find())

    if session_df.empty and global_df.empty:
        return "No data available", None, None, None, None, None, None, None, None

    # --- 1. Session vs Global Frequency ---
    freq_sess = session_df.groupby(session_df["timestamp"].dt.date).size().reset_index(name='Session')
    freq_glob = global_df.groupby(global_df["timestamp"].dt.date).size().reset_index(name='Global')
    freq_merged = pd.merge(freq_sess, freq_glob, on="timestamp", how="outer").fillna(0)
    freq_long = freq_merged.melt(id_vars="timestamp", var_name="Source", value_name="Count")
    fig_freq = px.line(freq_long, x="timestamp", y="Count", color="Source", title="Query Frequency: Session vs Global")

    # --- 2. Answer Length Histogram (Session only) ---
    fig_len = px.histogram(
        session_df,
        x="answer_length",
        nbins=20,
        title="Answer Length Distribution (Session)"
    )

    # --- 3. Multimodal Input Count (Session only) ---
    media_df = pd.DataFrame({
        "Modality": ["Image Used", "Table Used"],
        "Count": [session_df["used_image"].sum(), session_df["used_table"].sum()]
    })
    fig_media = px.bar(media_df, x="Modality", y="Count", title="Multimodal Inputs (Session)")

    # --- 4. Fallback Ratio (Session vs Global) ---
    fb_session = session_df["is_fallback"].value_counts().to_dict()
    fb_global = global_df["answer"].apply(lambda x: "I’m sorry, but I don’t have enough information" in x).value_counts().to_dict()

    fb_df = pd.DataFrame([
        {"Type": "Fallback", "Session": fb_session.get(True, 0), "Global": fb_global.get(True, 0)},
        {"Type": "Informative", "Session": fb_session.get(False, 0), "Global": fb_global.get(False, 0)}
    ])
    fb_long = fb_df.melt(id_vars="Type", var_name="Source", value_name="Count")
    fig_fb = px.bar(fb_long, x="Type", y="Count", color="Source", barmode="group", title="Fallbacks: Session vs Global")

    # --- 5. Top Queries Global ---
    top_qs = pd.DataFrame(global_df["query"].value_counts().reset_index())
    top_qs.columns = ["Query", "Frequency"]
    fig_top = px.bar(top_qs.head(10), x="Query", y="Frequency", title="Top Queries Globally")

    return "Analytics Updated", fig_freq, fig_len, fig_media, fig_fb, fig_top




# Interface
chat_tab = gr.Interface(
    fn=chroma_interface,
    inputs=[
        gr.Textbox(label="Ask a question"),
        gr.File(label="Upload an Image (Optional)", type="binary"),
        gr.File(label="Upload a Table (CSV, Optional)", type="binary")
    ],
    outputs=gr.Textbox(label="RAG Response"),
    title="RAG Chatbot",
    description="Ask a question related to your document corpus. Optionally include an image or table."
)

analytics_tab = gr.Interface(
    fn=show_analytics,
    inputs=[],
    outputs=[
        gr.Textbox(label="Summary"),
        gr.Plot(label="Query Frequency: Session vs Global"),
        gr.Plot(label="Answer Length Distribution (Session)"),
        gr.Plot(label="Multimodal Inputs (Session)"),
        gr.Plot(label="Fallbacks: Session vs Global"),
        gr.Plot(label="Top Global Queries")
    ],
)



gr.TabbedInterface([chat_tab, analytics_tab], ["Chat", "Analytics"]).launch(server_name="0.0.0.0", server_port=7860)
