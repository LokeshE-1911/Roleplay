# app/history.py
from datetime import datetime
chat_log = {}

def get_session_id():
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    if now not in chat_log:
        chat_log[now] = []
    return now

def log_message(session_id: str, message: str):
    chat_log[session_id].append(message)

def get_chat_history(session_id: str):
    return chat_log.get(session_id, [])