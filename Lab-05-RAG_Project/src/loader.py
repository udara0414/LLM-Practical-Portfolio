
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

PDF_FOLDER = Path("data/documents")

def load_documents():
    documents = []

    pdf_files = list(PDF_FOLDER.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError("No PDF files found in data/documents")

    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")

        loader = PyMuPDFLoader(str(pdf_file))
        pages = loader.load()

        documents.extend(pages)

    print(f"Total pages loaded: {len(documents)}")

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print("\nFirst page content:")
    print(docs[0].page_content[:1000])
