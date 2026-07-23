from fastapi import FastAPI

from app.core.config import settings

from app.api.v1.api import api_router

from app.middleware.request_logger import (
    RequestLoggerMiddleware
)



app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0"

)



app.include_router(

    api_router,

    prefix="/api/v1"

)



app.add_middleware(

    RequestLoggerMiddleware

)



@app.get("/")

def root():

    return {

        "message":
        "AI Tourism RAG API"

    }