import os
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

from ai import ask_ai

from buttons import start as start_button
from buttons import chats as chats_button
from buttons import new_chat

from commands import start, chats, help, about, back_to_bot


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def ai_message(update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text

    await update.message.reply_text(
        "⏳ جاري التفكير..."
    )

    response = ask_ai(message)

    await update.message.reply_text(
        response
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()


    # Commands
    start.register(app)
    chats.register(app)
    help.register(app)
    about.register(app)
    back_to_bot.register(app)


    # Buttons
    start_button.register(app)
    chats_button.register(app)
    new_chat.register(app)


    # AI messages
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            ai_message
        )
    )


    print("👑 KingAI Started")

    app.run_polling()


if __name__ == "__main__":
    main()
