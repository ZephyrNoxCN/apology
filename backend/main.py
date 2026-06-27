from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import json

app = FastAPI(title="道歉程序")

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

@app.get("/", response_class=HTMLResponse)
async def index():
    html_path = FRONTEND_DIR / "index.html"
    return html_path.read_text(encoding="utf-8")

@app.post("/api/forgive")
async def forgive():
    """Record forgiveness (placeholder for future KV storage)."""
    return {
        "status": "forgiven",
        "message": "已原谅 💖",
        "emoji": "😊"
    }
