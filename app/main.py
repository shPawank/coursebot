from fastapi import FastAPI
from pydantic import BaseModel
from app.answerer import chat_response
from app.session import ChatSession
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent
sessions = {}

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "static" / "index.html")
    
class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.post("/ask")
def ask_question(request: ChatRequest):
    if request.session_id not in sessions:
        sessions[request.session_id] = ChatSession()

    session = sessions[request.session_id]

    return chat_response(request.message, session)