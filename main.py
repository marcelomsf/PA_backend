from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


app = FastAPI()


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")

# uvicorn main:app --reload
from routes.auth_routes import auth_router
from routes.user_routes import user_router
from routes.word_routes import word_router
from routes.game_routes import game_router


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(word_router)
app.include_router(game_router)