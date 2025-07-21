from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/users")
async def read_users():
    """_summary_
    Esssa é a rota de listar todos os usuários.
    Returns:
        _type_: _description_
    """
    
    return {"message": "List of users"}
@user_router.get("/users/{user_id}")
async def read_user():
    """_summary_
    Esssa é a rota de informaçao do usuário.
    Returns:
        _type_: _description_
    """
    
    return {"message": "List of user"} 


