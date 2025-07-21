from fastapi import APIRouter, Depends, HTTPException

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/auth")
async def auth():
    """_summary_
    Esssa é a rota de autenticação.
    Returns:
        _type_: _description_
    """
    return {"message": "Authentication endpoint"}

@auth_router.post("/auth/singup")
async def singup():
    """_summary_
    Esssa é a rota de singup.
    Returns:
        _type_: _description_
    """
    return {"message": "singup endpoint"}

@auth_router.post("/auth/login")
async def login():
    """_summary_
    Esssa é a rota de login.
    Returns:
        _type_: _description_
    """
    return {"message": "login endpoint"}

@auth_router.get("/auth/refresh")
async def refresh():
    """_summary_
    Esssa é a rota de refresh.
    Returns:
        _type_: _description_
    """
    return {"message": "refresh endpoint"}