from fastapi import APIRouter, Response, Request
from app.main.model.user import LoginRequest
from app.main.service.auth import gen_auth_jwt_token, validate_credentials

auth_router = APIRouter(prefix='/auth')

@auth_router.post("/login")
async def do_login(login_creds: LoginRequest,response: Response):

    is_creds_valid = validate_credentials(login_creds.username, login_creds.password)
    if is_creds_valid:
        response.set_cookie(key="Authorization", value="JABAHUT")
        return {"message":"Logged in successfully!!"}
    else:
        response.delete_cookie("Authorization")
        return {"error": "Login Failed..."}

@auth_router.get("/printcookies")
async def read_cookies(request: Request):
    resp = {
        "Authorization": request.cookies.get('Authorization'),
        "USER_ID": request.cookies.get('USER_ID'),
    }
    return resp
