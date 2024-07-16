from sqlalchemy import Integer, ForeignKey, String, Column, TIMESTAMP
from datetime import datetime
from app.main.orm.base import Base
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import mapped_column
import enum
from sqlalchemy import Integer, Enum

class PostType(enum.Enum):
    post = "POST"
    comment = "COMMENT"

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    content = Column(String(255),nullable=False)
    type = Column(Enum(PostType))
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    repost_count = Column(Integer, default=0)
    quote_count = Column(Integer, default=0)
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())

class RePost(Base):
    __tablename__ = "repost"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    post_id = mapped_column(Integer, ForeignKey("post.id"))
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())

    __table_args__ = (
        UniqueConstraint('user_id', 'post_id', name='user_id_post_id_uc'),
    )


class QuotePost(Base):
    __tablename__ = "quotepost"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    parent_post_id = mapped_column(Integer, ForeignKey("post.id"))
    comment_post_id = mapped_column(Integer, ForeignKey("post.id"))
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())



class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    post_id = mapped_column(Integer, ForeignKey("post.id"))
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())

    __table_args__ = (UniqueConstraint('user_id', 'post_id', name='user_post_like_uc'),)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    parent_post_id = mapped_column(Integer, ForeignKey("post.id"))
    comment_post_id = mapped_column(Integer, ForeignKey("post.id"))
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())