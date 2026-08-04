from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_buttons():
    keyboard = [
        [
            InlineKeyboardButton(
                "💬 محادثة جديدة",
                callback_data="new_chat"
            )
        ],
        [
            InlineKeyboardButton(
                "🧠 المحادثات",
                callback_data="chats"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
