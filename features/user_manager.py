import json
import os
from datetime import datetime


USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    os.makedirs("data", exist_ok=True)

    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            users,
            file,
            ensure_ascii=False,
            indent=4
        )


def add_user(user_id, username=None):

    users = load_users()

    for user in users:
        if user["id"] == user_id:
            return False

    users.append({
        "id": user_id,
        "username": username,
        "joined": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_users(users)

    return True


def get_user(user_id):

    users = load_users()

    for user in users:
        if user["id"] == user_id:
            return user

    return None
