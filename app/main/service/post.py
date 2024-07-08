from app.main.util.database import get_local_session
from app.main.orm.post import Post

db_session = get_local_session()

def create_post(postinfo,user_id):
    post = Post(content=postinfo.content,user_id=user_id)
    db_session.add(post)
    db_session.commit()

    return post.id