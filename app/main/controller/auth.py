from fastapi import APIRouter, Response, Request
from app.main.model.user import LoginRequest


auth_router = APIRouter(prefix='/auth')

@auth_router.post("/login")
async def do_login(login_creds: LoginRequest,response: Response):
    response.set_cookie(key="Authorization", value="JABAHUT")
    response.set_cookie(key="USER_ID", value="1")

    return {"message":"Logged in successfully!!"}

@auth_router.get("/printcookies")
async def read_cookies(request: Request):
    resp = {
        "Authorization": request.cookies.get('Authorization'),
        "USER_ID": request.cookies.get('USER_ID'),
    }
    return resp
