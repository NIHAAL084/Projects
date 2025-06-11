# file: chroma_api_tool.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pathlib import Path

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# --- Your search function ---
def query_chroma(query: str, persist_directory: str, embedding_model: str, top_k: int) -> List[dict]:
    if not Path(persist_directory).exists():
        raise FileNotFoundError(f"Chroma DB not found at {persist_directory}")

    embeddings = OllamaEmbeddings(model=embedding_model)
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    results = vectordb.similarity_search_with_score(query, k=top_k)

    return [
        {
            "content": doc.page_content,
            "metadata": doc.metadata,
            "score": score
        }
        for doc, score in results
    ]

# --- FastAPI App ---
app = FastAPI(title="Chroma Vector Search API")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5
    persist_directory: str = r"C:\Users\nihaa\Documents\Projects\rag-chatbot-project\data\chroma"
    embedding_model: str = "mxbai-embed-large:latest"

class QueryResponseItem(BaseModel):
    content: str
    metadata: dict
    score: float

@app.post("/search", response_model=List[QueryResponseItem])
def search(request: QueryRequest):
    try:
        results = query_chroma(
            query=request.query,
            persist_directory=request.persist_directory,
            embedding_model=request.embedding_model,
            top_k=request.top_k
        )
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
