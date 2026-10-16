import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# A chat session remembers the conversation
chat = client.chats.create(model="gemini-3.1-flash-lite")

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text, "\n")