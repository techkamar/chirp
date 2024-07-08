from app.main.orm.base import Base
from app.main.util.database import get_connection

def create_all_tables():
    Base.metadata.create_all(get_connection())    