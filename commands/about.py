from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👑 KingAI\n\n"
        "🤖 بوت ذكاء اصطناعي مبني باستخدام Gemini API\n"
        "⚡ سريع وبسيط وسهل الاستخدام\n\n"
        "المطور: King Team"
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "about",
            about_command
        )
    )
