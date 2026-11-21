
from langchain_ollama import OllamaEmbeddings


def get_embedding_model():

    model = OllamaEmbeddings(
        model="qwen3-embedding:0.6b"
    )

    return model

