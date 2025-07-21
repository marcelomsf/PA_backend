from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

word_router = APIRouter(prefix="/words", tags=["words"])

@word_router.get("/words")
async def read_users():
    return {"message": "List of words"}

@word_router.get("/words/day_word")
async def day_word():
    return {"message": "Get the word of the day"}     
   
   
@word_router.get("/words/random_word")
async def random_word():
    return {"message": "Get the word for continue game"}  
