from fastapi import APIRouter, Depends, HTTPException
from models.db import Usuario 
from utils.dependencies import get_session
from main import bcrypt_context
from models.schemas import UsuarioSchema
from sqlalchemy.orm import Session

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
async def singup(usuario_schema: UsuarioSchema, session: Session = Depends(get_session)):
    """_summary
    Esssa é a rota de singup.
    Returns:
        _type_: _description_
    """
    usuario = session.query(Usuario).filter(Usuario.username == usuario_schema.nome).first()
    
    if usuario:
        # ja existe um usuario com esse email
        raise  HTTPException ( status_code=400 , detail ="Já existe um usuário cadastrado")
    else:
        senha_segura = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario( usuario_schema.username, usuario_schema.name, usuario_schema.email, usuario_schema.senha_segura, usuario_schema.ativo. usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return HTTPException ( status_code=200 , detail ="usuário cadastrado com sucesso")
    


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