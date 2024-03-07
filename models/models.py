from sqlalchemy import Column, Integer, String
from .database import Base, engine


class User(Base):
    __tablename__ = "Users"

    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, primary_key=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, nullable=False)
    event_name = Column(String, index=True, nullable=False)


Base.metadata.create_all(bind=engine)
