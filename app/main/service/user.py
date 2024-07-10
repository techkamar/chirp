from app.main.util.database import get_local_session
from app.main.orm.user import User
from app.main.orm.post import Post
db_session = get_local_session()

def create_user(userinfo):
    user = User(username=userinfo.username,password=userinfo.password,display_name = userinfo.display_name)
    db_session.add(user)
    db_session.commit()

    return user.id

def delete_user(user_id):
    # Delete all posts
    db_session.query(Post).filter(Post.user_id==user_id).delete()

    # Delete user
    db_session.query(User).filter(User.id==user_id).delete()

    db_session.commit()
    
    return "Done"

