from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, ForeignKey, String, Column, TIMESTAMP
from datetime import datetime


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255),unique=True, nullable=False)
    display_name = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
    created_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    updated_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
