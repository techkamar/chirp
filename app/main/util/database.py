import sqlalchemy
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = None

def get_connection():
    global engine
    if engine!=None:
        return engine
    
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = urllib.parse.quote_plus(os.getenv("DB_PASS"))
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")


    SQLALCHEMY_DATABASE_URL = (
        "postgresql://"
        + DB_USER
        + ":"
        + DB_PASS
        + "@"
        + DB_HOST
        + ":"
        + DB_PORT
        + "/"
        + DB_NAME
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_size=10,pool_recycle=1800,pool_pre_ping=True)
    return engine

def get_local_session():
    engine = get_connection()
    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return local_session()