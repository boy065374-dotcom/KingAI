from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def back_to_bot_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 Back to Bot",
                url="https://t.me/Diverse11Zbot"
            )
        ]
    ]

    await update.message.reply_text(
        "اضغط للرجوع إلى البوت الأساسي 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def register(application):
    from telegram.ext import CommandHandler

    application.add_handler(
        CommandHandler("back_to_bot", back_to_bot_command)
    )
