import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# The personalities you can choose from
PERSONAS = {
    "Friendly Tutor": "You are a friendly tutor for beginners. Explain things in simple words, use short answers, and end every reply with one fun fact.",
    "Cooking Assistant": "You are a helpful cooking assistant. Suggest simple recipes, give short step-by-step instructions, and mention common ingredient substitutes.",
    "Travel Guide": "You are an enthusiastic travel guide. Give practical tips, suggest places to visit, and keep answers short and friendly.",
}

st.title("My GenAI Chatbot")

# Create the client ONCE
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    st.session_state.persona = None


def start_chat(persona_name):
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(system_instruction=PERSONAS[persona_name]),
    )
    st.session_state.messages = []
    st.session_state.persona = persona_name


# Sidebar controls
persona = st.sidebar.selectbox("Choose a personality", list(PERSONAS.keys()))
if st.sidebar.button("Clear chat"):
    start_chat(persona)

# Start a fresh chat if the personality changed
if st.session_state.persona != persona:
    start_chat(persona)

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

    def stream_reply():
        for chunk in st.session_state.chat.send_message_stream(prompt):
            if chunk.text:
                yield chunk.text

    with st.chat_message("assistant"):
        reply = st.write_stream(stream_reply())

    st.session_state.messages.append({"role": "assistant", "content": reply})