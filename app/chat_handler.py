# app/chat_handler.py
from app.stage_scorer import detect_stage_and_score
from app.file_loader import get_product_info
from app.history import log_message, get_session_id
from app.gemini_wrapper import stream_response
import asyncio

async def handle_chat(text: str, role: str):
    session_id = get_session_id()
    log_message(session_id, f"{role}: {text}")

    context = get_product_info() if role == "seller" else ""
    stage, score = detect_stage_and_score(text, role)

    yield f"[Stage: {stage} | Score: {score} points]\n"

    async for chunk in stream_response(text, context):
        log_message(session_id, f"AI: {chunk}")
        yield chunk