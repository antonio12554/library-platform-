#database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
#link of database
from src.config import settings

Engine = create_engine(settings.databse_url)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=Engine,autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield(db)
    finally:
        db.close()