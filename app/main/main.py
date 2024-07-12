from fastapi import FastAPI
from app.main.controller.user import user_router
from app.main.controller.post import post_router
from app.main.controller.images import image_router
from app.main.util.tablemake import create_all_tables
from fastapi.middleware.cors import CORSMiddleware



create_all_tables()

origins = [
    "http://localhost:5173"
]


tags_metadata = [
    {
        "name": "Image",
        "description": "All APIs related to Images",
    },
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

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, tags=["User"], prefix="/api/v1")
app.include_router(post_router, tags=["Post"], prefix="/api/v1")
app.include_router(image_router, tags=["Image"], prefix="/api/v1")

