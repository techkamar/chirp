from sqlalchemy import Integer, ForeignKey, String, Column, TIMESTAMP
from datetime import datetime
from app.main.orm.base import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255),unique=True, nullable=False)
    display_name = Column(String(255),nullable=False)
    display_pic = Column(String,nullable=False, default="nodp")
    password = Column(String(255),nullable=False)
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
