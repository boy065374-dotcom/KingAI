from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def back_to_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⬅️ للرجوع إلى البوت الرئيسي:\n\n"
        "https://t.me/Diverse11Zbot"
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "back",
            back_to_bot
        )
    )
