from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler


async def new_chat_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["creating_chat"] = True

    await query.message.reply_text(
        "➕ اكتب اسم المحادثة الجديدة:"
    )


async def new_chat_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("creating_chat"):

        chat_name = update.message.text

        context.user_data["creating_chat"] = False
        context.user_data["current_chat"] = chat_name

        await update.message.reply_text(
            f"✅ تم إنشاء المحادثة:\n\n💬 {chat_name}"
        )


def register(application):
    application.add_handler(
        CallbackQueryHandler(
            new_chat_button,
            pattern="^new_chat$"
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            new_chat_name
        )
    )
