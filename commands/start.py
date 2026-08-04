from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("🤖 Chat AI", callback_data="chat_ai"),
            InlineKeyboardButton("💬 Chats", callback_data="chats")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("❓ Help", callback_data="help")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👑 Welcome to KingAI\n\n"
        "🤖 مساعدك الذكي بالذكاء الاصطناعي\n\n"
        "اختر من القائمة:",
        reply_markup=reply_markup
    )


def register(application):
    from telegram.ext import CommandHandler

    application.add_handler(
        CommandHandler("start", start_command)
    )
