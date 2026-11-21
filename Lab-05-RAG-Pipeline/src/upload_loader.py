from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

UPLOAD_FOLDER = Path("data/uploads")

def load_uploaded_documents():
    documents = []

    pdf_files = list(UPLOAD_FOLDER.glob("*.pdf"))

    for pdf_file in pdf_files:
        print(f"Loading uploaded PDF: {pdf_file.name}")

        loader = PyMuPDFLoader(str(pdf_file))
        pages = loader.load()

        documents.extend(pages)

    print(f"Total uploaded pages: {len(documents)}")

    return documents