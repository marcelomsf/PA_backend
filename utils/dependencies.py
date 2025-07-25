from fastapi import Depends ,HTTPException
from models.db import db
from sqlalchemy.orm import sessionmaker, Session
from models.db import Usuario
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM , oauth2_schema

def get_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
        
        
def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(get_session)):
    try:        
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username = dic_info.get("sub")
    except JWTError as error:
        print(error)
        raise HTTPException (status_code=401, detail="Acesso negado")
    usuario = session.query(Usuario).filter(Usuario.username == username ).first()
    if not usuario:
            raise HTTPException(status_code=401, detail="Acesso inválido")
    return usuario 
