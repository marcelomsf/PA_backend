from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.db import Usuario, Palavra
from utils.dependencies import  verificar_token , get_session
from models.schemas import PalavraSchema
from sqlalchemy.orm import Session
import random

word_router = APIRouter(prefix="/words", tags=["words"])

@word_router.get("/")
async def read_users():
    return {"message": "List of words"}

@word_router.get("/day_word")
async def day_word( session: Session = Depends(get_session)):
    palavras = session.query(Palavra).all()
    print(len(palavras))
    random_offset = random.randint(0, len(palavras) - 1)
    print(random_offset)
    random_word = session.query(Palavra).filter(Palavra.id == random_offset).first()
    
    print(random_word.palavra)
    return {"palavra": random_word.palavra}   
   
   
@word_router.get("/random_word")
async def random_word( usuario: Usuario = Depends(verificar_token), session: Session = Depends(get_session)):
    palavras = session.query(Palavra).all()
    print(len(palavras))
    random_offset = random.randint(0, len(palavras) - 1)
    print(random_offset)
    random_word = session.query(Palavra).filter(Palavra.id == random_offset).first()
    
    print(random_word.palavra)
    return {"palavra": random_word.palavra}



@word_router.post("/add_word")
async def add_word(palavra_schema: PalavraSchema, usuario: Usuario = Depends(verificar_token), session: Session = Depends(get_session)):
    nova_palavra = Palavra( palavra_schema.palavra, palavra_schema.data)
    session.add(nova_palavra)
    session.commit()
    return {"message": "palavra adicionada" + palavra_schema.palavra }  
