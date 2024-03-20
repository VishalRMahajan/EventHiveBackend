import razorpay
from os import getenv
from dotenv import load_dotenv
from secrets import token_hex
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.profile import router as profile_router
from routes.fest import router as fest_router
from routes.auth import manager

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


@app.get("/pay/{amount}", response_class=HTMLResponse, dependencies=[Depends(manager)])
async def payment(request: Request, amount: int, user=Depends(manager)):
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


app.include_router(router=auth_router)
app.include_router(router=profile_router)
app.include_router(router=fest_router)
