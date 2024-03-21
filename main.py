import razorpay
from os import getenv
from dotenv import load_dotenv
from secrets import token_hex
from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.profile import router as profile_router
from routes.fest import router as fest_router
from routes.auth import manager
from models.models import UserEvent
from models.database import database

load_dotenv()

RZP_KEY = getenv("RZP_KEY")
RZP_SECRET = getenv("RZP_SECRET")

client = razorpay.Client(auth=(RZP_KEY, RZP_SECRET))

templates = Jinja2Templates(directory="templates")

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/pay", response_class=HTMLResponse)
async def payment_by_email(request: Request, amount: int, email: str, event_name: str,committee :str):
    """Endpoint to make payments"""
    print(event_name)
    data = {
        "amount": amount * 100,
        "currency": "INR",
        "receipt": token_hex(3),
        "notes": {"user_id": email, "event_name": event_name}
    }
    print(data)
    order = client.order.create(data=data)
    return templates.TemplateResponse(
        "pay.html", {"request": request, "order": order, "email": email, "event_name": event_name, "committee": committee}
    )


@app.get("/pay/{amount}", response_class=HTMLResponse, dependencies=[Depends(manager)])
async def payment_by_user(request: Request, amount: int, user=Depends(manager)):
    """Endpoint to make payments"""
    data = {
        "amount": amount * 100,
        "currency": "INR",
        "receipt": token_hex(3),
        "notes": {"user_id": user.email}
    }
    order = client.order.create(data=data)
    return templates.TemplateResponse(
        "pay.html", {"request": request, "order": order}
    )
@app.get("/verify_payment")
async def verify_payment(order_id: str,payment_id: str, payment_sign: str):
    """Endpoint to verify payments"""
    print("inside verify_payment")
    print(order_id, payment_id, payment_sign)
    try:
        payment = client.payment.fetch(payment_id)
        client.utility.verify_payment_signature(payment)
        return {"message": "Payment successful"}
    except Exception as e:
        return {"message": "Payment failed"}

@app.post("/addeventdb")
async def addeventdb(data: dict):
    print(data)
    email = data.get("email")
    event_name = data.get("event_name")
    committee = data.get("committee")
    user_event = UserEvent(email=email, event_name=event_name, committee=committee)
    database.add(user_event)
    try:
        database.commit()
        return {"message": "Event added successfully"}
    except:
        database.rollback()
        return {"message": "Event already exists"}

@app.post("/checkifregistered")
async def checkifregistered(email: str , event_name : str, committee : str):
    user_event_exists = database.query(database.query(UserEvent).filter(UserEvent.email == email, UserEvent.event_name == event_name,UserEvent.committee == committee).exists()).scalar()
    print("User Event is", user_event_exists)
    if user_event_exists:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"You are registered for event {event_name}"})
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "You are not registered for this event"})

app.include_router(router=auth_router)
app.include_router(router=profile_router)
app.include_router(router=fest_router)



