from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from features import chat_manager


async def new_chat_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.callback_query.answer()

    user_id = update.effective_user.id

    chat_manager.create_chat(user_id)

    await update.callback_query.message.reply_text(
        "🧠 تم بدء محادثة جديدة.\n\n"
        "اكتب رسالتك الآن لـ KingAI 🤖"
    )


def register(app):

    app.add_handler(
        CallbackQueryHandler(
            new_chat_button,
            pattern="^new_chat$"
        )
    )
