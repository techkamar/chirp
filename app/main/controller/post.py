from fastapi import APIRouter, Request
from app.main.service.post import create_post,get_posts_by_username,get_all_posts,like_post_by_id
from app.main.model.post import CreatePost
import app.main.util.userinfoutil as UserInfoUtil

post_router = APIRouter(prefix='/post')

@post_router.get("s")
async def get_posts():
    return get_all_posts()

@post_router.get("s/{username}")
async def get_posts_by_uname(username):
    return get_posts_by_username(username)

@post_router.post("")
async def make_post(post:CreatePost, request:Request):
    user_id = UserInfoUtil.get_user_id(request)
    return create_post(post,user_id)

@post_router.post("/{post_id}/like")
async def like_post(request:Request,post_id):
    post_id = int(post_id)
    user_id = UserInfoUtil.get_user_id(request)
    return like_post_by_id(post_id,user_id)