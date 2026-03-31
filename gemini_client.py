from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found")

genai.configure(api_key=api_key)

# ✅ Updated model
model = genai.GenerativeModel("models/gemini-1.5-pro")     # more accurate
def get_llm_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM Error: {e}"