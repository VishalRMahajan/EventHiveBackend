from sqlalchemy import Column, Integer, String,event, Table, MetaData
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

    event_name = Column(String, index=True, nullable=False,primary_key=True)
    committee = Column(String, index=True, nullable=False)
    contact_person = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    date = Column(String, index=True, nullable=False)
    time = Column(String, index=True, nullable=False)
    ticket_price = Column(String, index=True, nullable=False)
    venue = Column(String, index=True, nullable=False)
    contact_number = Column(String, index=True, nullable=False)


class UserEvent(Base):
    __tablename__ = "user_event"

    email = Column(String, index=True, nullable=False, primary_key=True)
    event_name = Column(String, index=True, nullable=False, primary_key=True)
    committee = Column(String, index=True, nullable=False)




"""def after_insert_listener(mapper, connection, target):
    meta = MetaData()
    table = Table(
        target.event_name, meta,
        Column('first_name', String(50)),
        Column('last_name', String(50)),
        Column('email', String(50)),
    )
    meta.create_all(engine)

def create_user_email_table(mapper, connection, target):
    meta = MetaData()
    table = Table(
        target.email, meta,
        Column('event_name', String(50)),
        Column('committee', String(50)),
    )
    meta.create_all(engine)

event.listen(User, 'after_insert', create_user_email_table)
event.listen(Event, 'after_insert', after_insert_listener)"""


Base.metadata.create_all(bind=engine)
