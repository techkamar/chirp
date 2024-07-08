from sqlalchemy import Integer, ForeignKey, String, Column, TIMESTAMP
from datetime import datetime
from app.main.orm.base import Base
from sqlalchemy.orm import mapped_column

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    content = Column(String(255),nullable=False)
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
