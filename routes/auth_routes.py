from fastapi import APIRouter, Depends, HTTPException

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/auth")
async def auth():
    """_summary_
    Esssa é a rota de autenticação.
    Returns:
        _type_: _description_
    """
    return {"message": "Authentication endpoint"}