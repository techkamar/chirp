from pydantic import BaseModel

class CreatePost(BaseModel):
    content: str


class GetLikesByUserIds(BaseModel):
    post_ids : list