from app.main.util.database import get_local_session
from app.main.orm.post import Post
from app.main.orm.user import User
from app.main.orm.like import Like
from app.main.orm.comment import Comment
from sqlalchemy import func

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
    result = db_session.query(Post.id,Post.content,Post.created_date,func.count(Like.id)).join(Like,isouter=True).group_by(Post.id).all()
    for id,content,created_date,likecount in result:
        posts.append({'id':id,'content':content,'likedby':likecount,'created_date':created_date})
    return posts
    
def like_post_by_id(post_id,user_id):
    like = Like(user_id=user_id, post_id=post_id)
    db_session.add(like)
    db_session.commit()


def create_post_comment(user_id,post_id,newPost):
    comment_post = Post(content=newPost.content,user_id=user_id)
    db_session.add(comment_post)
    db_session.flush()
    db_session.refresh(comment_post)

    comment = Comment(user_id=user_id, parent_post_id = post_id, comment_post_id=comment_post.id)
    db_session.add(comment)
    db_session.commit()

    return comment_post.id