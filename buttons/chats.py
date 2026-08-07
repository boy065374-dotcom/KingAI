from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from features import chat_manager


async def chats_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.callback_query.answer()

    user_id = update.effective_user.id

    chats = chat_manager.get_saved_chats(user_id)

    if not chats:
        await update.callback_query.message.reply_text(
            "💬 لا توجد محادثات محفوظة حاليا"
        )
        return

    text = "💬 المحادثات المحفوظة:\n\n"

    for index, chat in enumerate(chats, start=1):
        text += f"📌 محادثة رقم {index}\n"
        text += f"🕒 {chat['ended_at']}\n"
        text += f"📝 عدد الرسائل: {len(chat['messages'])}\n\n"

    await update.callback_query.message.reply_text(text)


def register(app):

    app.add_handler(
        CallbackQueryHandler(
            chats_button,
            pattern="^chats$"
        )
    )
