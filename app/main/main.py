from fastapi import FastAPI
from app.main.controller.user import user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")