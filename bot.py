import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    filters,
    ContextTypes
)

from ai import ask_ai

from buttons import start, chats, new_chat


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def ai_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    await update.message.reply_text("⏳ جاري التفكير...")

    response = ask_ai(user_message)

    await update.message.reply_text(response)


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # تسجيل الأزرار
    start.register(app)
    chats.register(app)
    new_chat.register(app)

    # استقبال رسائل المستخدم
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            ai_message
        )
    )

    print("👑 KingAI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
