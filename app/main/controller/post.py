from fastapi import APIRouter, Request, Depends
from app.main.controller.auth import validate_auth_login
from app.main.service.post import (
    create_post,
    get_posts_by_username,
    get_all_posts,
    like_post_by_id,
    create_post_comment,
    unlike_post_by_id,
    get_post_comments,
    get_single_post,
    get_like_user_id_by_post_ids
)
from app.main.model.post import CreatePost,GetLikesByUserIds
import app.main.util.userinfoutil as UserInfoUtil

post_router = APIRouter(prefix='/post')

# APIs related to Post
@post_router.get("s")
async def get_posts():
    return get_all_posts()

@post_router.get("s/{username}")
async def get_posts_by_uname(username):
    return get_posts_by_username(username)

@post_router.post("")
async def make_post(post:CreatePost, user_id=Depends(validate_auth_login)):
    return create_post(post,user_id)

@post_router.get("/{post_id}")
async def get_post(post_id:str):
    return get_single_post(post_id)

# APIs related to Like
@post_router.post("/{post_id}/like")
async def like_post(post_id:int,user_id=Depends(validate_auth_login)):
    return like_post_by_id(post_id,user_id)

@post_router.post("/like/userids")
async def get_user_ids_by_postids(post_ids: GetLikesByUserIds):
    return get_like_user_id_by_post_ids(post_ids.post_ids)

@post_router.post("/{post_id}/unlike")
async def unlike_post(request:Request,post_id: int):
    user_id = UserInfoUtil.get_user_id(request)
    unlike_post_by_id(post_id,user_id)


# APIs related to Comments
@post_router.post("/{post_id}/comment")
async def create_comment(newPost:CreatePost, post_id:int, user_id=Depends(validate_auth_login)):
    return create_post_comment(user_id,post_id,newPost)

@post_router.get("/{post_id}/comments")
async def get_all_comments_of_post(post_id: int):
    return get_post_comments(post_id)


# APIs related to Repost
