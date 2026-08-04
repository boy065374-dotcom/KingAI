import os
from dotenv import load_dotenv

from telegram.ext import Application

from commands import start
from commands import help
from commands import about

from buttons import chats
from buttons import new_chat


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    start.register(app)
    help.register(app)
    about.register(app)

    # Buttons
    chats.register(app)
    new_chat.register(app)

    print("👑 KingAI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
