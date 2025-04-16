# app/routes.py
from fastapi import APIRouter, Form, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from app.chat_handler import handle_chat
from app.file_loader import load_product_data

router = APIRouter()

@router.post("/chat")
async def chat(text: str = Form(...), role: str = Form(...)):
    return StreamingResponse(handle_chat(text, role), media_type="text/plain")

@router.post("/upload_product")
async def upload_product(file: UploadFile = File(...)):
    load_product_data(file.file)
    return JSONResponse(content={"message": "Product file loaded."})