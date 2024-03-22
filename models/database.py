from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()
DB_URL = getenv("DB_URL")

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
database = Session(bind=engine)

def get_db():
    """Get a database connection to the database using a context manager"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()