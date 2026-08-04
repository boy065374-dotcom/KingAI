from telegram import Update
from telegram.ext import ContextTypes


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
👑 KingAI

🤖 بوت ذكاء اصطناعي يعمل بواسطة Gemini.

✨ المميزات:
• محادثات متعددة
• حفظ المحادثات
• ذاكرة للمستخدم
• نظام قريب من ChatGPT

🎮 Developed by King Games

🚀 Version: 1.0
        """
    )


def register(application):
    from telegram.ext import CommandHandler

    application.add_handler(
        CommandHandler("about", about_command)
    )
