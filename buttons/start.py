from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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

    if update.message:
        await update.message.reply_text(
            "👑 أهلاً بك في KingAI\n\nاختر من القائمة:",
            reply_markup=reply_markup
        )

    elif update.callback_query:
        await update.callback_query.message.edit_text(
            "👑 أهلاً بك في KingAI\n\nاختر من القائمة:",
            reply_markup=reply_markup
        )
