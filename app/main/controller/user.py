from fastapi import APIRouter
from app.main.model.user import CreatUser
user_router = APIRouter(prefix='/user')


@user_router.get("s")
async def get_users():
    return []

@user_router.post("")
async def add_user(user:CreatUser):
    print(user)