from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.profile import router as profile_router

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

app.include_router(router=auth_router)
app.include_router(router=profile_router)
