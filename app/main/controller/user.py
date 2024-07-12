from fastapi import APIRouter,UploadFile
from app.main.model.user import CreatUser
from app.main.service.user import create_user,delete_user,get_single_user, post_user_dp, get_all_users
user_router = APIRouter(prefix='/user')


@user_router.get("s")
async def get_users():
    return get_all_users()

@user_router.post("")
async def add_user(user:CreatUser):
    return create_user(user)

@user_router.delete("/{user_id}")
async def del_user(user_id:int):
    return delete_user(user_id)

@user_router.get("/{user_id}")
async def get_user(user_id:int):
    return get_single_user(user_id)

@user_router.post("/{user_id}/display_picture")
async def post_user_display_picture(user_id:int, file:UploadFile):
    return post_user_dp(user_id,file)

