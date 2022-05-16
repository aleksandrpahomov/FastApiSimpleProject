import uvicorn
from fastapi import FastAPI
from app.handlers import router

def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app

app = get_application()