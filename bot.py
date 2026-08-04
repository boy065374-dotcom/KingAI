import os
from dotenv import load_dotenv

from telegram.ext import Application

from commands import start, help, about
from buttons import chats, new_chat

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    start.register(app)
    help.register(app)
    about.register(app)

    chats.register(app)
    new_chat.register(app)

    print("👑 KingAI Running")

    app.run_polling()


if __name__ == "__main__":
    main()
