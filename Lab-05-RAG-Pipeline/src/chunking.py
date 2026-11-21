
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.loader import load_documents


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Original pages: {len(documents)}")
    print(f"Total chunks created: {len(chunks)}")

    return chunks


if __name__ == "__main__":

    documents = load_documents()

    chunks = split_documents(documents)

    print("\nFirst chunk:")
    print(chunks[0].page_content)

    print("\nChunk metadata:")
    print(chunks[0].metadata)
