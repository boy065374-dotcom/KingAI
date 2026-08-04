# features/memory.py

def format_memory(messages, limit=20):
    """
    يحول آخر رسائل لصيغة مناسبة للـ AI
    """

    recent_messages = messages[-limit:]

    memory = ""

    for msg in recent_messages:
        role = msg.get("role")
        content = msg.get("content")

        if role == "user":
            memory += f"You:\n{content}\n\n"

        elif role == "assistant":
            memory += f"Bot:\n{content}\n\n"

    return memory


def add_message(messages, role, content):
    """
    إضافة رسالة جديدة للذاكرة المؤقتة
    """

    messages.append(
        {
            "role": role,
            "content": content
        }
    )

    return messages
