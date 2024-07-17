from fastapi import APIRouter, Response, Request
from app.main.model.user import LoginRequest
from app.main.service.auth import gen_auth_jwt_token, validate_credentials, get_expiry_timestamp,validate_login

auth_router = APIRouter(prefix='/auth')

@auth_router.post("/login")
async def do_login(login_creds: LoginRequest,response: Response):
    is_creds_valid, user_details = validate_credentials(login_creds.username, login_creds.password)
    if is_creds_valid:
        payload_json = {
            'id': user_details['id'],
            'exp': get_expiry_timestamp()
        }
        token = gen_auth_jwt_token(payload_json)
        response.set_cookie(key="Authorization", value=token)
        return {"message":"Logged in successfully!!", "success": True}
    else:
        response.delete_cookie("Authorization")
        return {"error": "Login Failed...Username or password is invalid", "success": False}

@auth_router.get("/logout")
async def do_logout(response: Response):
    response.delete_cookie("Authorization")
    return {"message": "User Logged Out"}

@auth_router.get("/validate-login")
async def validate_auth_login(request: Request):
    auth_jwt = request.cookies.get('Authorization')
    user_id = validate_login(auth_jwt)
    return user_id