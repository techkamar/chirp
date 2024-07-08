from pydantic import BaseModel

class CreatUser(BaseModel):
    username: str
    display_name: str
    password: str