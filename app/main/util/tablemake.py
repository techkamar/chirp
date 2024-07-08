from app.main.util.database import get_connection
from app.main.orm.user import Base

def create_all_tables():
    Base.metadata.create_all(get_connection())    