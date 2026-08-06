from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes


async def chats_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.callback_query.answer()

    await update.callback_query.message.reply_text(
        "💬 لا توجد محادثات محفوظة حاليا"
    )


def register(app):

    app.add_handler(
        CallbackQueryHandler(
            chats_button,
            pattern="^chats$"
        )
    )
