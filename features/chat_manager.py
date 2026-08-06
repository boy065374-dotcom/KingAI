import json
import os
from datetime import datetime


CHATS_FILE = "data/chats.json"


def load_chats():
    if not os.path.exists(CHATS_FILE):
        return []

    with open(CHATS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_chats(chats):
    os.makedirs("data", exist_ok=True)

    with open(CHATS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            chats,
            file,
            ensure_ascii=False,
            indent=4
        )


def create_chat(user_id):

    chats = load_chats()

    chat = {
        "user_id": user_id,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": []
    }

    chats.append(chat)

    save_chats(chats)

    return chat


def add_message(user_id, user_message, ai_message):

    chats = load_chats()

    user_chat = None

    for chat in chats:
        if chat["user_id"] == user_id:
            user_chat = chat
            break

    if user_chat is None:
        user_chat = create_chat(user_id)
        chats = load_chats()

        for chat in chats:
            if chat["user_id"] == user_id:
                user_chat = chat
                break

    user_chat["messages"].append({
        "user": user_message,
        "ai": ai_message,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_chats(chats)


def get_chat(user_id):

    chats = load_chats()

    for chat in chats:
        if chat["user_id"] == user_id:
            return chat

    return None
