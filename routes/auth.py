from datetime import datetime, timedelta
from models.database import database
from models.models import Student, Committee
from fastapi import APIRouter, Depends, status
from typing import Dict
from fastapi.responses import JSONResponse
import bcrypt
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from pydantic import BaseModel
from sqlalchemy.exc import NoResultFound

SECRET = "36d25b15c99e0684166cdfc27e1b9f724a223c6fa810230d"
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

    if usertype == "student":
        already = database.query(Student).filter(Student.email == email).first()
        if already:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Student already exists"})
        else:
            student = Student(first_name=fname, last_name=lname, email=email, password=password)
            database.add(student)
            database.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Student registered successfully"})
    elif usertype == "committee":
        already = database.query(Committee).filter(Committee.email == email).first()
        if already:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Committee already exists"})
        else:
            committee = Committee(first_name=fname, last_name=lname, email=email, password=password)
            database.add(committee)
            database.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Committee registered successfully"})
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Invalid usertype"})

class UserLoginRequest(BaseModel):
    """Request model for the login endpoint"""
    usertype: str
    email: str
    password: str

@manager.user_loader()
def query_user(email_id, usertype):
    try:
        if usertype == "student":
            return database.query(Student).filter_by(email=email_id).one()
        elif usertype == "committee":
            return database.query(Committee).filter_by(email=email_id).one()
    except NoResultFound:
        raise NoResultFound("User not found")

@router.post("/login")
async def login(usertype: str, data: OAuth2PasswordRequestForm = Depends()):
    print(data)
    usertype = usertype.lower()
    email = data.username.lower()
    password = data.password
    try:
        user = query_user(email, usertype)
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


@router.post("/verify")
async def data(user=Depends(manager)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content="You are logged in as " + user.email
    )