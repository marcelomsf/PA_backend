from fastapi import FastAPI, HTTPException

app = FastAPI()
# uvicorn main:app --reload
from routes.auth_routes import auth_router
from routes.user_routes import user_router


app.include_router(auth_router)
app.include_router(user_router)