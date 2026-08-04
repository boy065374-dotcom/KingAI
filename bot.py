import os
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    MessageHandler,
    filters
)

from ai import ask_ai

from commands import help
from commands import about

from buttons import chats
from buttons import new_chat


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def ai_chat(update, context):
    user_message = update.message.text

    await update.message.reply_text("🤖 جاري التفكير...")

    response = ask_ai(user_message)

    await update.message.reply_text(response)


def main():

    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not found")
        return

    app = Application.builder().token(BOT_TOKEN).build()


    # Commands
    help.register(app)
    about.register(app)


    # Buttons
    chats.register(app)
    new_chat.register(app)


    # Gemini AI
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            ai_chat
        )
    )


    print("👑 KingAI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
