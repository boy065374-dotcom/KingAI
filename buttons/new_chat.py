from telegram.ext import CallbackQueryHandler


async def new_chat_button(update, context):
    query = update.callback_query

    await query.answer()

    await query.message.reply_text(
        "🧠 اكتب رسالتك الآن لـ KingAI"
    )


def register(app):
    app.add_handler(
        CallbackQueryHandler(
            new_chat_button,
            pattern="^new_chat$"
        )
    )
