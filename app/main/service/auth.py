import jwt
import os
import time
from fastapi import HTTPException
from app.main.orm.user import User
from app.main.util.database import get_local_session

db_session = get_local_session()


def gen_auth_jwt_token(payload_json):
    token = jwt.encode(
        payload=payload_json,
        key = os.getenv("JWT_SECRET_KEY")
    )
    return token

def validate_credentials(username, password):
    result = db_session.query(User).filter(User.username==username).filter(User.password==password).all()
    if len(result)==0:
        return False, {}
    
    user_details = {}
    for user in result:
        user_details['id'] = user.id

    return True, user_details

def validate_login(auth_jwt):
    try:
        token = jwt.decode(auth_jwt,os.getenv("JWT_SECRET_KEY"),algorithms=["HS256"])
        return token['id']
    except:
        raise HTTPException(status_code=401, detail="User needs to be logged in")

def get_expiry_timestamp():
    minutes = int(os.getenv("JWT_KEY_EXPIRY_IN_MINUTES","10")) # Default is 10
    return int(time.time())+(60*minutes)