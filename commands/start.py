from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👑 أهلاً بك في KingAI 🤖\n\n"
        "أنا مساعدك بالذكاء الاصطناعي.\n"
        "اكتب أي رسالة وسأساعدك 🧠\n\n"
        "استخدم /help لمعرفة الأوامر."
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )
