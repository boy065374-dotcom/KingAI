import os
import json
import uuid
from datetime import datetime


DATA_FOLDER = "data"


def get_user_folder(user_id):
    return os.path.join(DATA_FOLDER, str(user_id))


def create_user(user_id):
    user_folder = get_user_folder(user_id)
    chats_folder = os.path.join(user_folder, "chats")

    os.makedirs(chats_folder, exist_ok=True)

    return user_folder


def create_chat(user_id, title):
    create_user(user_id)

    chat_id = str(uuid.uuid4())[:8]

    chat_data = {
        "id": chat_id,
        "title": title,
        "created_at": str(datetime.now()),
        "messages": []
    }

    path = os.path.join(
        get_user_folder(user_id),
        "chats",
        f"{chat_id}.json"
    )

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            chat_data,
            file,
            ensure_ascii=False,
            indent=4
        )

    return chat_id


def get_user_chats(user_id):
    chats_folder = os.path.join(
        get_user_folder(user_id),
        "chats"
    )

    if not os.path.exists(chats_folder):
        return []

    chats = []

    for file_name in os.listdir(chats_folder):
        if file_name.endswith(".json"):
            with open(
                os.path.join(chats_folder, file_name),
                "r",
                encoding="utf-8"
            ) as file:
                chats.append(json.load(file))

    return chats
