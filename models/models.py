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
    committee = Column(String, index=True, nullable=False)
    contact_person = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    date = Column(String, index=True, nullable=False)
    time = Column(String, index=True, nullable=False)
    ticket_price = Column(Integer, index=True, nullable=False)
    venue = Column(String, index=True, nullable=False)
    contact_number = Column(Integer, index=True, nullable=False)



Base.metadata.create_all(bind=engine)
