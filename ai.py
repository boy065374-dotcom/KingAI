import os
import requests
from dotenv import load_dotenv

from features.memory import get_memory

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"


def ask_ai(message, user_id=None):
    try:

        final_message = message

        if user_id:
            memories = get_memory(user_id)

            if memories:
                memory_text = "\n".join(memories)

                final_message = f"""
ذاكرة المستخدم:
{memory_text}

رسالة المستخدم:
{message}
"""

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": final_message
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code != 200:
            return f"خطأ API:\n{response.text}"

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]


    except Exception as e:
        return f"حدث خطأ:\n{e}"
