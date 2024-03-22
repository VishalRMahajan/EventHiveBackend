from datetime import datetime, timedelta
from models.database import database
from models.models import User
from fastapi import APIRouter, Depends, status
from typing import Dict
from fastapi.responses import JSONResponse
import bcrypt
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from pydantic import BaseModel
from sqlalchemy.exc import NoResultFound
from dotenv import load_dotenv
load_dotenv()

SECRET = getenv("SECRET")
router = APIRouter(prefix="/auth")
manager = LoginManager(SECRET, "/auth/login")

@router.post("/register")
async def register(data : Dict):
    usertype = data.get("usertype")
    fname = data.get("fname")
    lname = data.get("lname")
    email = data.get("email")
    password = data.get("password")
    #salt = bcrypt.gensalt()
    #hash_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    already = database.query(User).filter(User.email == email).first()
    if already:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Student already exists"})
    else:
        user = User(first_name=fname, last_name=lname, email=email, password=password, role=usertype)
        database.add(user)
        database.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Student registered successfully"})

class UserLoginRequest(BaseModel):
    """Request model for the login endpoint"""
    usertype: str
    email: str
    password: str

@manager.user_loader()
def query_user(email_id):
    try:
        return database.query(User).filter_by(email=email_id).one()
    except NoResultFound:
        raise NoResultFound("User not found")

@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username.lower()
    password = data.password
    try:
        user = query_user(email)
    except NoResultFound:
        print("User not found")
        raise InvalidCredentialsException

    if password != user.password:
        raise InvalidCredentialsException
    else:
        access_token = manager.create_access_token(data={"sub": email}, expires=timedelta(hours=3))
        now = datetime.utcnow() + timedelta(hours=5, minutes=30)
        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "access_token": access_token,
                    "token_type": "bearer",
                },
        )


@router.get("/protected")
async def protected_route(user=Depends(manager)):
    if user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "Role": user.role,
                "email": user.email,
            },
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content="You are not logged in"
        )