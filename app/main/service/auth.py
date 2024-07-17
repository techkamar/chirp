import jwt
import os
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
        return False
    
    return True