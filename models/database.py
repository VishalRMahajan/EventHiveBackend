import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()
DB_URL = "postgresql://vishal:993uhp!_-b9dQjD@35.200.156.179:5432/eventhive-db"

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