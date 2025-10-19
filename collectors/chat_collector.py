def collect_chat_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        messages = f.readlines()
    return [{"message": msg.strip()} for msg in messages if msg.strip()]