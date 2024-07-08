from fastapi import APIRouter
from app.main.service.post import create_post
from app.main.model.post import CreatePost

post_router = APIRouter(prefix='/post')

@post_router.get("s")
async def get_posts():
    return []

@post_router.post("")
async def make_post(post:CreatePost):
    return create_post(post,1)