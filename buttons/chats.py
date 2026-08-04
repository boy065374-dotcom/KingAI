from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler


async def chats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "➕ New Chat",
                callback_data="new_chat"
            )
        ]
    ]

    await update.message.reply_text(
        "💬 Your Chats\n\n"
        "لا توجد محادثات محفوظة حاليًا.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def chats_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "chats":
        await chats_command(update, context)


def register(application):
    application.add_handler(
        CommandHandler("chats", chats_command)
    )

    application.add_handler(
        CallbackQueryHandler(chats_button)
    )
