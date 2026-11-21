
import streamlit as st
import os

from src.chatbot import ask_question
from src.vectorstore import add_uploaded_documents


st.set_page_config(
    page_title="NSBM RAG Chatbot",
    page_icon="📚"
)

st.title("📚 NSBM RAG Chatbot")

st.write("Upload PDF documents and ask questions.")

# PDF Upload
uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

# Save uploaded PDFs
if uploaded_files:

    upload_folder = "data/uploads"
    os.makedirs(upload_folder, exist_ok=True)

    for uploaded_file in uploaded_files:

        file_path = os.path.join(
            upload_folder,
            uploaded_file.name
        )

        if not os.path.exists(file_path):

            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

    st.success("PDF files saved successfully!")

    # Add PDFs to Knowledge Base
    if st.button("Add PDFs to Knowledge Base"):

        with st.spinner("Processing uploaded PDFs..."):
            add_uploaded_documents()

        st.success("PDF processing completed!")


# Ask Questions
question = st.text_input("Enter your question:")

if st.button("Ask"):

    if question:

        with st.spinner("Generating answer..."):

            answer, sources = ask_question(question)

        st.write("### Answer")
        st.write(answer)

        st.write("### Sources")

        for source in sources:

            st.write(
                f"📄 {source['file']} - Page {source['page']}"
            )

    else:
        st.warning("Please enter a question.")
