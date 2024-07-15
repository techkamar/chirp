from fastapi import HTTPException
from app.main.util.database import get_local_session
from app.main.orm.post import Post,PostType,Like,Comment
from app.main.orm.user import User
from sqlalchemy import func

db_session = get_local_session()

def create_post(postinfo,user_id):
    post = Post(content=postinfo.content,user_id=user_id, type= PostType.post)
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
    result = db_session.query(
        Post.id,Post.content,Post.created_date,Post.like_count, Post.comment_count, Post.repost_count, Post.quote_count, Post.user_id
        ).filter(Post.type==PostType.post).order_by(Post.created_date.desc()).all()
    for id,content,created_date,likecount,comment_count, share_count, quote_count,user_id in result:
        posts.append({'id':id,'content':content,'likedby':likecount,'commentedby':comment_count,'sharedby':share_count, 'quotedby':quote_count,'user_id':user_id,'created_date':created_date})
    return posts

def get_single_post(post_id):
    posts = db_session.query(
        Post.id,Post.content,Post.created_date,Post.like_count, Post.comment_count, Post.repost_count, Post.quote_count, Post.user_id
        ).filter(Post.id==post_id).all()
    
    for id,content,created_date,likecount,comment_count, share_count, quote_count,user_id in posts:
        return {
            'id':id,
            'content':content,
            'likedby':likecount,
            'commentedby':comment_count,
            'sharedby':share_count,
            'quotedby':quote_count,
            'user_id':user_id,
            'created_date':created_date
        }
    
    
def like_post_by_id(post_id,user_id):
    like = Like(user_id=user_id, post_id=post_id)
    try:
        db_session.add(like)
        db_session.query(Post).filter(Post.id==post_id).update({Post.like_count:Post.like_count+1})
        db_session.commit()
    except:
        db_session.rollback()
        raise HTTPException(status_code=405, detail="Item not found")

def unlike_post_by_id(post_id,user_id):
    db_session.query(Like).filter(Like.post_id==post_id).filter(Like.user_id==user_id).delete()
    db_session.query(Post).filter(Post.id==post_id).update({Post.like_count:Post.like_count-1})
    db_session.commit()


def create_post_comment(user_id,post_id,newPost):
    comment_post = Post(content=newPost.content,user_id=user_id, type=PostType.comment)
    db_session.add(comment_post)
    db_session.flush()
    db_session.refresh(comment_post)

    comment = Comment(user_id=user_id, parent_post_id = post_id, comment_post_id=comment_post.id)
    db_session.add(comment)

    # increment comment count
    db_session.query(Post).filter(Post.id==post_id).update({Post.comment_count:Post.comment_count+1})

    db_session.commit()

    return comment_post.id

def get_post_comments(post_id):
    comments = []
    sub_query = db_session.query(Comment.comment_post_id).join(Post,onclause=Comment.parent_post_id==Post.id).filter(Comment.parent_post_id==post_id)
    comment_posts = db_session.query(Post).filter(Post.id.in_(sub_query)).all()
    for curr_post in comment_posts:
        comments.append(
            {
                'id': curr_post.id,
                'content': curr_post.content,
                'user_id': curr_post.user_id,
                'likedby':curr_post.like_count,
                'commentedby':curr_post.comment_count,
                'sharedby':curr_post.repost_count, 
                'quotedby':curr_post.quote_count,
                'created_date': curr_post.created_date
            }
        )
    return comments
