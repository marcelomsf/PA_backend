from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/users")
async def read_users():
    return {"message": "List of users"}     
