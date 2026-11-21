
from langchain_chroma import Chroma

from src.loader import load_documents
from src.upload_loader import load_uploaded_documents
from src.chunking import split_documents
from src.embeddings import get_embedding_model


VECTORSTORE_PATH = "vectorstore/chroma_qwen3"


def create_vectorstore():

    print("Loading documents...")

    documents = load_documents()

    print("Creating chunks...")

    chunks = split_documents(documents)

    print("Loading embedding model...")

    embedding_model = get_embedding_model()

    print("Saving embeddings to ChromaDB...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTORSTORE_PATH,
        collection_name="nsbm_handbook"
    )

    print("Vector database created successfully!")

    print("Total stored chunks:", vectorstore._collection.count())

    return vectorstore


def add_uploaded_documents():

    print("Loading uploaded PDFs...")

    documents = load_uploaded_documents()

    if not documents:
        print("No uploaded PDFs found!")
        return

    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embedding_model,
        collection_name="nsbm_handbook"
    )

    existing_data = vectorstore.get(include=["metadatas"])

    existing_sources = {
        metadata.get("source")
        for metadata in existing_data["metadatas"]
        if metadata.get("source")
    }

    new_documents = [
        doc for doc in documents
        if doc.metadata.get("source") not in existing_sources
    ]

    if not new_documents:
        print("All uploaded PDFs are already in the database!")
        return

    print("Creating chunks...")

    chunks = split_documents(new_documents)

    print("Adding new documents...")

    vectorstore.add_documents(chunks)

    print("New PDFs added successfully!")

    print("Total stored chunks:", vectorstore._collection.count())


if __name__ == "__main__":

    create_vectorstore()

