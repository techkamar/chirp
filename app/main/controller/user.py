from fastapi import APIRouter
from app.main.model.user import CreatUser
from app.main.service.user import create_user,delete_user
user_router = APIRouter(prefix='/user')


@user_router.get("s")
async def get_users():
    return []

@user_router.post("")
async def add_user(user:CreatUser):
    return create_user(user)

@user_router.delete("/{user_id}")
async def del_user(user_id:int):
    return delete_user(user_id)