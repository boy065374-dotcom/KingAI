from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from features import chat_manager


async def end_chat_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.callback_query.answer()

    user_id = update.effective_user.id

    saved = chat_manager.end_chat(user_id)

    if saved:
        await update.callback_query.message.reply_text(
            "✅ تم إنهاء المحادثة وحفظها."
        )
    else:
        await update.callback_query.message.reply_text(
            "⚠️ لا توجد محادثة حالية لحفظها."
        )


def register(app):

    app.add_handler(
        CallbackQueryHandler(
            end_chat_button,
            pattern="^end_chat$"
        )
    )
