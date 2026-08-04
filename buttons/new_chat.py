from telegram.ext import CallbackQueryHandler


async def new_chat_button(update, context):

    await update.callback_query.answer()

    await update.callback_query.message.reply_text(
        "🧠 اكتب رسالتك الآن لـ King AI"
    )


def register(app):

    app.add_handler(
        CallbackQueryHandler(
            new_chat_button,
            pattern="^new_chat$"
        )
    )
