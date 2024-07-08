from fastapi import APIRouter
from app.main.service.post import create_post,get_posts_by_username,get_all_posts
from app.main.model.post import CreatePost

post_router = APIRouter(prefix='/post')

@post_router.get("s")
async def get_posts():
    return get_all_posts()

@post_router.get("s/{username}")
async def get_posts_by_uname(username):
    return get_posts_by_username(username)

@post_router.post("")
async def make_post(post:CreatePost):
    return create_post(post,2)