import os
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

from ai import ask_ai

from features import user_manager
from features import chat_manager

from commands import start, chat, help, about, back_to_bot

from buttons import start as start_button
from buttons import chats as chats_button
from buttons import new_chat
from buttons import end_chat


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def ai_message(update: ContextTypes.DEFAULT_TYPE, context):

    user_id = update.effective_user.id

    user_manager.add_user(user_id)

    user_message = update.message.text

    await update.message.reply_text(
        "⏳ جاري التفكير..."
    )

    response = ask_ai(
        user_message,
        user_id
    )

    chat_manager.add_message(
        user_id,
        user_message,
        response
    )

    await update.message.reply_text(
        response
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()


    # Commands
    start.register(app)
    chat.register(app)
    help.register(app)
    about.register(app)
    back_to_bot.register(app)


    # Buttons
    start_button.register(app)
    chats_button.register(app)
    new_chat.register(app)
    end_chat.register(app)


    # AI Messages
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
