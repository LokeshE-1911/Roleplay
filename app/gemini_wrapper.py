# app/gemini_wrapper.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

async def stream_response(user_input: str, context: str):
    chat = model.start_chat(history=[])
    prompt = f"Context:\n{context}\nUser: {user_input}"
    async for chunk in chat.stream_content(prompt):
        yield chunk.text