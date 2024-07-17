from pydantic import BaseModel

class CreatUser(BaseModel):
    username: str
    display_name: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str