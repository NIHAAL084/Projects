#import necessary libraries
import pandas as pd
import json
from pathlib import Path
from fpdf import FPDF

# Define constants for file names
# These constants represent the names of the CSV files used in the project.
DOC_CSV      = 'documents.csv'
MP_CSV       = 'multi_passage_answer_questions.csv'
SP_CSV       = 'single_passage_answer_questions.csv'
NA_CSV       = 'no_answer_questions.csv'

# Define groups of documents to process
# These tuples represent the start and end indices of document groups for processing.
GROUPS = [(0, 8), (6, 14), (12, 20)]

# Load the documents CSV file into a DataFrame
# This DataFrame will contain the documents with their respective indices and source URLs.
docs_df = pd.read_csv(DOC_CSV)

# 1) Build documents.txt, documents.md, and documents.pdf  
for i, (start, end) in enumerate(GROUPS, start=1):
    chunk = docs_df.iloc[start:end]
    
    # TXT
    with open(f'docs_part{i}.txt', 'w', encoding='utf-8') as f:
        for _, r in chunk.iterrows():
            f.write(f"Document {r['index']} (Source: {r['source_url']}):\n{r['text']}\n\n")
    
    # Markdown
    with open(f'docs_part{i}.md', 'w', encoding='utf-8') as f:
        for _, r in chunk.iterrows():
            f.write(f"## Document {r['index']}\n")
            f.write(f"**Source**: {r['source_url']}\n\n{r['text']}\n\n")
    
    # PDF
    pdf = FPDF()
    pdf.set_auto_page_break(True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for _, r in chunk.iterrows():
        # Clean text for PDF: drop any char not in Latin-1
        title = f"Document {r['index']} (Source: {r['source_url']})"
        body  = r['text'].encode('latin-1', 'ignore').decode('latin-1')
        
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(0, 10, title)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, body)
        pdf.ln(5)
    
    pdf.output(f'docs_part{i}.pdf')

# 2) Build sample-queries.json
mp = pd.read_csv(MP_CSV)
sp = pd.read_csv(SP_CSV)
na = pd.read_csv(NA_CSV)

queries = []
qid = 1
for df, has_ans in [(mp, True), (sp, True), (na, False)]:
    for _, r in df.iterrows():
        entry = {
            "query_id": f"q{qid}",
            "document_index": int(r["document_index"]),
            "question": r["question"],
            "answer": r["answer"] if has_ans else "I’m sorry, but I don’t have enough information on that topic right now. Could you try rephrasing your question, or let me know if you’d like me to connect you with our support team for more details?"
        }
        queries.append(entry)
        qid += 1

with open("sample-queries.json", "w", encoding="utf-8") as f:
    json.dump(queries, f, indent=2)



