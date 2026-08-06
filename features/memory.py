import json
import os


MEMORY_FILE = "data/memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):

    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            memory,
            file,
            ensure_ascii=False,
            indent=4
        )


def add_memory(user_id, info):

    memory = load_memory()

    user_memory = None

    for item in memory:
        if item["user_id"] == user_id:
            user_memory = item
            break

    if user_memory is None:

        user_memory = {
            "user_id": user_id,
            "memory": []
        }

        memory.append(user_memory)


    user_memory["memory"].append(info)

    save_memory(memory)


def get_memory(user_id):

    memory = load_memory()

    for item in memory:
        if item["user_id"] == user_id:
            return item["memory"]

    return []


def clear_memory(user_id):

    memory = load_memory()

    memory = [
        item for item in memory
        if item["user_id"] != user_id
    ]

    save_memory(memory)
