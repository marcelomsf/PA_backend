from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.db import Usuario 
from utils.dependencies import  verificar_token

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/")
async def read_users():
    """_summary_
    Esssa é a rota de listar todos os usuários.
    Returns:
        _type_: _description_
    """
    
    return {"message": "List of users"}



@user_router.get("/user")
async def read_user(usuario: Usuario = Depends(verificar_token)):
    """_summary_
    Esssa é a rota de informaçao do usuário.
    Returns:
        _type_: _description_
    """
    id_user  = usuario.id
    username = usuario.username
    email = usuario.email
    admin = usuario.is_admin
    return {"id" : id_user,
            "username": username,
             "email" : email,
             "admin" : admin
             } 
    
@user_router.get("/{user_id}")
async def read_user_by_id():
    """_summary_
    Esssa é a rota de informaçao do usuário.
    Returns:
        _type_: _description_
    """
    
    return {"message": "List of user"} 

