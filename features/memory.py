import json
import os

MEMORY_FILE = "data/memory.json"


def _load():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):

    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_memory(user_id):

    data = _load()

    uid = str(user_id)

    return data.get(uid, [])


def add_memory(user_id, text):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        data[uid] = []

    if text not in data[uid]:
        data[uid].append(text)

    _save(data)


def remove_memory(user_id, text):

    data = _load()

    uid = str(user_id)

    if uid in data and text in data[uid]:
        data[uid].remove(text)

        _save(data)


def clear_memory(user_id):

    data = _load()

    uid = str(user_id)

    if uid in data:
        data[uid] = []

        _save(data)
