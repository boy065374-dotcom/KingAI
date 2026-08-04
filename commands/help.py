from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🤖 KingAI Help

الأوامر:

/start - تشغيل البوت
/help - المساعدة
/about - معلومات عن البوت
/back_to_bot - الرجوع للبوت الأساسي

💬 المحادثات:
استخدم زر Chats لإدارة محادثاتك.
        """
    )


def register(application):
    from telegram.ext import CommandHandler

    application.add_handler(
        CommandHandler("help", help_command)
    )
