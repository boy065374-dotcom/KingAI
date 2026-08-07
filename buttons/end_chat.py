from telegram.ext import CallbackQueryHandler


async def end_chat_button(update, context):

    await update.callback_query.answer()

    await update.callback_query.message.reply_text(
        "✅ تم إنهاء المحادثة وحفظها."
    )


def register(app):

    app.add_handler(
        CallbackQueryHandler(
            end_chat_button,
            pattern="^end_chat$"
        )
    )
