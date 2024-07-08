from fastapi import FastAPI
from app.main.controller.user import user_router
from app.main.controller.post import post_router
from app.main.util.tablemake import create_all_tables



create_all_tables()



tags_metadata = [
    {
        "name": "User",
        "description": "All APIs related to user",
    },
    {
        "name": "Post",
        "description": "All APIs related to Posts by user",
    }
]
app = FastAPI(
    title="Chirp Core MS",
    openapi_tags=tags_metadata
)

app.include_router(user_router, tags=["User"], prefix="/api/v1")
app.include_router(post_router, tags=["Post"], prefix="/api/v1")
