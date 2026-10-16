import os
from dotenv import load_dotenv
from google import genai

# Load the API key from the .env file
load_dotenv()

# Connect to Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Send a prompt and get a response
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain what a generative AI application is in two sentences."
)

print(response.text)