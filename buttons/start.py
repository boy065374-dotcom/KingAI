from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("🤖 New Chat", callback_data="new_chat"),
            InlineKeyboardButton("💬 Chats", callback_data="chats")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👑 أهلاً بك في KingAI\n\nاختر من القائمة:",
        reply_markup=reply_markup
    )


def register(app):
    from telegram.ext import CommandHandler

    app.add_handler(
        CommandHandler(
            "start",
            start_button
        )
    )
