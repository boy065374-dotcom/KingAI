# features/gemini.py

import os


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


async def ask_gemini(prompt, memory=""):
    """
    إرسال رسالة إلى Gemini
    """

    full_prompt = f"""
You are KingAI, an AI assistant.

Previous conversation:
{memory}

User message:
{prompt}

Answer the user clearly and helpfully.
"""

    # هنا هنضيف كود اتصال Gemini API لاحقًا
    # بعد اختيار مكتبة Gemini المناسبة

    response = "Gemini response will be here."

    return response
