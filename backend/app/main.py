from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router
from app.middleware.request_logger import RequestLoggerMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

# -----------------------------
# CORS Middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Logger Middleware
# -----------------------------
app.add_middleware(
    RequestLoggerMiddleware
)

# -----------------------------
# API Routes
# -----------------------------
app.include_router(
    api_router,
    prefix="/api/v1"
)

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "AI Tourism RAG API"
    }