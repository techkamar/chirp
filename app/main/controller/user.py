from fastapi import APIRouter
from app.main.model.user import CreatUser
from app.main.service.user import create_user
user_router = APIRouter(prefix='/user')


@user_router.get("s")
async def get_users():
    return []

@user_router.post("")
async def add_user(user:CreatUser):
    create_user(user)