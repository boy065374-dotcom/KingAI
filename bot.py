import os
from telegram.ext import Application

from buttons import start
from buttons import help
from buttons import about
from buttons import back_to_bot


TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = Application.builder().token(TOKEN).build()

    # Register buttons/modules
    start.register(app)
    help.register(app)
    about.register(app)
    back_to_bot.register(app)

    print("KingAI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
