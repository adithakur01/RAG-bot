import streamlit as st
from rag_backend import query_gemini

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")

st.title("📚 Retrieval-Augmented Generation Chatbot")
st.write(
    "Ask questions about your uploaded documents. "
    "The system will retrieve relevant chunks and answer using Gemini."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Type your question here...")

# Show history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])

# Handle new input
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        answer = query_gemini(user_input)

    with st.chat_message("assistant"):
        st.write(answer)

    # Save history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": answer})
