from app.main.util.database import get_local_session
from app.main.orm.post import Post
from app.main.orm.user import User

db_session = get_local_session()

def create_post(postinfo,user_id):
    post = Post(content=postinfo.content,user_id=user_id)
    db_session.add(post)
    db_session.commit()

    return post.id

def get_posts_by_username(username):
    posts = []
    result = db_session.query(Post).join(User).filter(User.username==username).all()
    for entry in result:
        posts.append({'id':entry.id,'content':entry.content})
    return posts

def get_all_posts():
    posts = []
    result = db_session.query(Post).all()
    for entry in result:
        posts.append({'id':entry.id,'content':entry.content})
    return posts
    
