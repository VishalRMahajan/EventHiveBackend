
from models.database import database
from models.models import Event
from fastapi import APIRouter, status
from typing import Dict
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


router = APIRouter(prefix="/fest")

@router.post("/add")
async def addevent(data : Dict):
    event_name = data.get("event_name")
    committee = data.get("committee_name")
    contact_person = data.get("contact_person")
    description = data.get("description")
    date = data.get("Date")
    time = data.get("Time")
    ticket_price = data.get("Ticket_price")
    venue = data.get("venue")
    contact_number = data.get("phone")

    already = database.query(Event).filter(Event.event_name == event_name).first()
    if already:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Event already exists"})
    else:
        event = Event(event_name=event_name, committee=committee, contact_person=contact_person, description=description, date=date, time=time, ticket_price=ticket_price, venue=venue, contact_number=contact_number)
        database.add(event)
        database.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Event added successfully"})


@router.get("/all")
async def get_all_events():
    all_events = []
    events = database.query(Event).all()
    for event in events:
        all_events.append({
            "event_name": event.event_name,
            "committee": event.committee,
            "contact_person": event.contact_person,
            "description": event.description,
            "date": event.date,
            "time": event.time,
            "ticket_price": event.ticket_price,
            "venue": event.venue,
            "contact_number": event.contact_number
        })
    return all_events

#to fect fest
@router.get("/fetch")
async def fetch_event(event_name: str):
    event = database.query(Event).filter(Event.event_name == event_name).first()
    if event:
        return {
            "event_name": event.event_name,
            "committee": event.committee,
            "contact_person": event.contact_person,
            "description": event.description,
            "date": event.date,
            "time": event.time,
            "ticket_price": event.ticket_price,
            "venue": event.venue,
            "contact_number": event.contact_number
        }
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Event not found"})

#get ticket_price using event_name
@router.get("/ticket_price")
async def get_ticket_price(event_name: str):
    event = database.query(Event).filter(Event.event_name == event_name).first()
    if event:
        return {
            "ticket_price": event.ticket_price
        }
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Event not found"})