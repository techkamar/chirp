from app.main.util.database import get_local_session
from app.main.orm.user import User
db_session = get_local_session()

def create_user(userinfo):
    user = User(username=userinfo.username,password=userinfo.password,display_name = userinfo.display_name)
    db_session.add(user)
    db_session.commit()