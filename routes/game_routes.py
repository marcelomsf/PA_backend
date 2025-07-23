from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

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
     
