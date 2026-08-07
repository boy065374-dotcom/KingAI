import json
import os
from datetime import datetime

CHATS_FILE = "data/chats.json"


def _load():
    if not os.path.exists(CHATS_FILE):
        return {}

    with open(CHATS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):
    os.makedirs("data", exist_ok=True)

    with open(CHATS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def create_chat(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        data[uid] = {
            "current": [],
            "saved": []
        }

    data[uid]["current"] = []

    _save(data)


def add_message(user_id, user_text, ai_text):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        create_chat(user_id)
        data = _load()

    data[uid]["current"].append(
        {
            "user": user_text,
            "ai": ai_text,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )

    _save(data)


def end_chat(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        return False

    if len(data[uid]["current"]) == 0:
        return False

    data[uid]["saved"].append(
        {
            "ended_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": data[uid]["current"]
        }
    )

    data[uid]["current"] = []

    _save(data)

    return True


def get_saved_chats(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        return []

    return data[uid]["saved"]


def get_current_chat(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        return []

    return data[uid]["current"]
