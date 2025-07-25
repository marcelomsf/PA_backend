from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utils.dependencies import get_session
from sqlalchemy.orm import Session
from models.schemas import JogoSchema
from models.db import Jogo

game_router = APIRouter(prefix="/games", tags=["games"])

@game_router.get("/")
async def read_games():
    """_summary_
    Essa é a  para listar todos os jogos do sistema.
    Returns:
        _type_: _description_
    """
    return {"message": "List of Games"}

@game_router.get("/{user_id}")
async def list_games_by_user():
    """_summary_
    Essa é a  para listar todos os jogos por usuario.
    Returns:
        _type_: _description_
    """
    return {"message": "List of Games by user"}     
     
     
@game_router.post("/saveGame")
async def save_game_result(jogo_schena : JogoSchema , session : Session = Depends(get_session)):
    novo_jogo  =  Jogo (id_usuario=jogo_schena.id_usuario, palavra=jogo_schena.palavra, tentativas=jogo_schena.tentativas, acertou=jogo_schena.acerto, pontos=jogo_schena.pontos)
    session.add(novo_jogo)
    session.commit()
    return {"mensagem" : f"Jogo salvo com sucesso: {jogo_schena.id_usuario}"}
    

     
