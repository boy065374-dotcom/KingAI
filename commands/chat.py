from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["chat_mode"] = True

    await update.message.reply_text(
        "🤖 تم تشغيل وضع المحادثة.\n"
        "اكتب رسالتك وسيقوم KingAI بالرد عليك."
    )


def register(application):
    application.add_handler(
        CommandHandler("chat", chat_command)
    )
