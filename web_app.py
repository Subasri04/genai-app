import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

st.title("My GenAI Chatbot")

# Create the client and chat ONCE, and keep them together
if "chat" not in st.session_state:
    st.session_state.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="You are a friendly tutor for beginners. Explain things in simple words, use short answers, and end every reply with one fun fact."
        ),
    )
    st.session_state.messages = []

# Show the earlier messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box at the bottom of the page
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)