from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 أوامر KingAI:\n\n"
        "/help - عرض الأوامر\n"
        "/chats - عرض المحادثات\n"
        "/back - الرجوع للبوت\n"
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )
