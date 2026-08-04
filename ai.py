import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def ask_ai(message):
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"حدث خطأ: {e}"
