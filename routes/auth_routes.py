from fastapi import APIRouter, Depends, HTTPException
from models.db import Usuario 
from utils.dependencies import get_session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():
    """_summary_
    Esssa é a rota de autenticação.
    Returns:
        _type_: _description_
    """
    return {"message": "Authentication endpoint"}

@auth_router.post("/singup")
async def singup(username : str, name: str, senha : str, email: str, session = Depends(get_session)):
    """_summary
    Esssa é a rota de singup.
    Returns:
        _type_: _description_
    """
    usuario = session.query(Usuario).filter(Usuario.username == username).first()
    
    if usuario:
        # ja existe um usuario com esse email
        return {"mensagem" : "Já existe um usuário cadastrado"}
    else:
        senha_segura = bcrypt_context.hash(senha)
        novo_usuario = Usuario( username, name, email, senha_segura)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem" : "usuário cadastrado com sucesso"}
    
    return {"message": "singup endpoint"}

@auth_router.post("/login")
async def login():
    """_summary_
    Esssa é a rota de login.
    Returns:
        _type_: _description_
    """
    return {"message": "login endpoint"}

@auth_router.get("/refresh")
async def refresh():
    """_summary_
    Esssa é a rota de refresh.
    Returns:
        _type_: _description_
    """
    return {"message": "refresh endpoint"}