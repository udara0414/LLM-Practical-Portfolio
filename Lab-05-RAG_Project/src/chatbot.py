
from langchain_ollama import ChatOllama
from pathlib import Path
from src.retriever import hybrid_search


def get_chatbot():

    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    return llm


def ask_question(question):

    llm = get_chatbot()

    # Retrieve relevant documents using Hybrid Search
    documents = hybrid_search(question)

    # Create context
    context = "\n\n".join(
        document.page_content[:500]
        for document in documents[:3]
    )

    # Create prompt
    prompt = f"""
    You are an NSBM Computing Awards Handbook assistant.

    Answer the user's question using ONLY the context below.

    If the answer is not available in the context,
    say: "I could not find this information in the handbook."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # Generate answer
    response = llm.invoke(prompt)

    # Collect source documents
    sources = []

    for document in documents:

        source_name = Path(
            document.metadata.get("source", "Unknown")
        ).name

        page_number = document.metadata.get("page", 0) + 1

        source_info = {
            "file": source_name,
            "page": page_number
        }

        if source_info not in sources:
            sources.append(source_info)

    return response.content, sources


if __name__ == "__main__":

    question = input("\nAsk a question about the handbook: ")

    print("\nGenerating answer...\n")

    answer, sources = ask_question(question)

    print("Chatbot Answer:")
    print(answer)

    print("\nSources:")

    for source in sources:
        print(f"{source['file']} - Page {source['page']}")

