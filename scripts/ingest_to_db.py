from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from pathlib import Path

def ingest_to_chroma(
    file_paths: list[str],
    persist_directory: str = "./chroma_db",
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    embedding_model: str = "mxbai-embed-large:latest"
) -> None:
    """
    Load documents from given file paths, split into chunks, generate embeddings using Ollama,
    and store them persistently in a local Chroma database.

    Args:
        file_paths (list[str]): List of file paths (.pdf, .txt, .md) to ingest.
        persist_directory (str): Directory to persist Chroma DB. Defaults to './chroma_db'.
        chunk_size (int): Token-based chunk size for splitting. Defaults to 1000.
        chunk_overlap (int): Token overlap between chunks. Defaults to 200.
        embedding_model (str): Ollama model to use for embeddings. Defaults to 'mxbai-embed-large:latest'.
    """
    # Initialize text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # Initialize embedding function
    embeddings = OllamaEmbeddings(model=embedding_model)

    # Prepare persistent Chroma vector store
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    # Process each file
    for path_str in file_paths:
        path = Path(path_str)
        if not path.exists():
            print(f"Warning: {path} does not exist, skipping.")
            continue

        # Select loader based on extension
        if path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(path))
        elif path.suffix.lower() == ".txt":
            loader = TextLoader(str(path), encoding="utf-8")
        elif path.suffix.lower() in [".md", ".markdown"]:
            loader = UnstructuredMarkdownLoader(str(path))
        else:
            print(f"Unsupported file type: {path.suffix}, skipping.")
            continue

        # Load and split documents
        docs = loader.load()
        chunks = splitter.split_documents(docs)

        # Add to Chroma
        vectordb.add_documents(chunks)
        print(f"Ingested {len(chunks)} chunks from {path.name}")

    # Persist the Chroma database
    print(f"Chroma DB persisted at '{persist_directory}'")



files = [r"C:\Users\nihaa\Documents\Projects\rag-chatbot-project\data\sample-documents\docs_part1.pdf", r"C:\Users\nihaa\Documents\Projects\rag-chatbot-project\data\sample-documents\docs_part2.txt", r"C:\Users\nihaa\Documents\Projects\rag-chatbot-project\data\sample-documents\docs_part3.md"]
ingest_to_chroma(files, persist_directory= r"C:\Users\nihaa\Documents\Projects\rag-chatbot-project\data\chroma")
