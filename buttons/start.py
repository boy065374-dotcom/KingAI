from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🧠 محادثة جديدة",
                callback_data="new_chat"
            ),
            InlineKeyboardButton(
                "💬 المحادثات",
                callback_data="chats"
            )
        ],
        [
            InlineKeyboardButton(
                "🛑 إنهاء الدردشة",
                callback_data="end_chat"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👑 أهلاً بك في KingAI 🤖\n\n"
        "أنا مساعدك بالذكاء الاصطناعي 🧠\n"
        "اختر من القائمة:",
        reply_markup=reply_markup
    )


def register(app):

    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )
