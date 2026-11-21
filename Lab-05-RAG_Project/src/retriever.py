
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever

from src.embeddings import get_embedding_model
from src.loader import load_documents
from src.chunking import split_documents


VECTORSTORE_PATH = "vectorstore/chroma_qwen3"


def get_retriever():

    print("Loading embedding model...")

    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embedding_model,
        collection_name="nsbm_handbook"
    )

    vector_retriever = vectorstore.as_retriever(
        search_kwargs={"k": 10}
    )

    print("Building BM25 index...")

    documents = load_documents()
    chunks = split_documents(documents)

    bm25_retriever = BM25Retriever.from_documents(chunks)
    bm25_retriever.k = 10

    return vector_retriever, bm25_retriever


def hybrid_search(question):

    vector_retriever, bm25_retriever = get_retriever()

    vector_results = vector_retriever.invoke(question)

    expanded_query = (
        question +
        " ASSESSMENT 50 Examination E1 "
        "30 Coursework C1 20 Practical P1"
    )

    bm25_results = bm25_retriever.invoke(expanded_query)

    # Reciprocal Rank Fusion (RRF)
    scores = {}
    documents = {}

    for results, weight in [
        (vector_results, 1),
        (bm25_results, 3)
    ]:

        for rank, document in enumerate(results):

            key = (
                document.metadata.get("source"),
                document.metadata.get("page"),
                document.page_content
            )

            scores[key] = scores.get(key, 0) + weight / (60 + rank + 1)
            documents[key] = document

    ranked_results = sorted(
        scores,
        key=scores.get,
        reverse=True
    )

    return [documents[key] for key in ranked_results[:5]]


if __name__ == "__main__":

    question = "What is the assessment structure for PUSL3205?"

    print("\nSearching using hybrid retrieval...")

    results = hybrid_search(question)

    for i, document in enumerate(results):

        print(f"\n--- Result {i + 1} ---")
        print(document.page_content[:500])
        print("Source:", document.metadata.get("source"))
        print("Page:", document.metadata.get("page", -1) + 1)
