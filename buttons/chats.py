from telegram.ext import CallbackQueryHandler


async def chats_button(update, context):
    query = update.callback_query

    await query.answer()

    await query.message.reply_text(
        "💬 لا توجد محادثات محفوظة حاليا"
    )


def register(app):
    app.add_handler(
        CallbackQueryHandler(
            chats_button,
            pattern="^chats$"
        )
    )
