from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 أوامر KingAI:\n\n"
        "💬 /chats - عرض المحادثات\n"
        "⬅️ /back - الرجوع إلى البوت الرئيسي\n"
        "❓ /help - عرض قائمة الأوامر\n\n"
        "اكتب أي رسالة وسأرد عليك بالذكاء الاصطناعي 🧠"
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )
