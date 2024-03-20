from models.database import database
from fastapi import APIRouter, Depends, status
from typing import Dict
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/profile")
from routes.auth import manager

@router.get("/me")
async def protected_route(user=Depends(manager)):
    if user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "email": user.email,
                "role": user.role,
                "fname": user.first_name,
                "lname": user.last_name,
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content="You are not logged in"
        )

@router.post("/update")
async def update(data : Dict, user=Depends(manager)):
    fname = data.get("fname")
    lname = data.get("lname")

    user.first_name = fname
    user.last_name = lname
    database.commit()
