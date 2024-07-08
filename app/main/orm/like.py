from sqlalchemy import Integer, ForeignKey, String, Column, TIMESTAMP
from datetime import datetime
from app.main.orm.base import Base
from sqlalchemy.orm import mapped_column

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    post_id = mapped_column(Integer, ForeignKey("post.id"))
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
