from fastapi import APIRouter, Depends, HTTPException
from models.db import Usuario 
from utils.dependencies import get_session
from main import bcrypt_context , ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES , SECRET_KEY
from models.schemas import UsuarioSchema, LoginScheme
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta , timezone


auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_toker(username, duration_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) ):
    #jJWT
    data_expiracao = datetime.now(timezone.utc) + duration_token
    dic_info = {"sub" : username, "exp" : data_expiracao}
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_codificado

def verificar_token(token , session):
    # To DO Verificar se o token é valido 
    # TO DO Extrair o ID do Usuário
    usuario = session.query(Usuario).filter(Usuario.id == 3 ).first()    
    return usuario 


def autenticar_usuario(username, senha , session):
    usuario = session.query(Usuario).filter(Usuario.username == username).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.hashed_password):
        return False
    
    return usuario

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
async def login(login_schema: LoginScheme, session: Session = Depends(get_session)):
    """_summary_
    Esssa é a rota de login.
    Returns:
        _type_: _description_
    """
    usuario = autenticar_usuario(login_schema.username, login_schema.hashed_password , session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Username não encontrado!")
    else:
        access_token = criar_toker(usuario.username)
        refresh_token = criar_toker(usuario.username, duration_token=timedelta(days=7))
        return {"access_token" : access_token,
                "refresh_token" : refresh_token,
                "token_type" : "Bearer"
                }


@auth_router.get("/refresh")
async def refresh(token,  session: Session = Depends(get_session)):
    """_summary_
    Esssa é a rota de refresh.
    Returns:
        _type_: _description_
    """
    usuario = verificar_token(token, session )
    access_token = criar_toker(usuario.username)
    return {"access_token" : access_token,
                "token_type" : "Bearer"
                }