from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def chats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "💬 لا توجد محادثات محفوظة حاليا"
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "chats",
            chats_command
        )
    )
