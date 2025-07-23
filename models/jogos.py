from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base , DeclarativeBase


Base = declarative_base()


class Jogo(Base):
    __tablename__ = 'jogos'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    palavra = Column(String, index=True, nullable=False)
    tentativas = Column(Integer, default=0)
    acertou = Column(Boolean, default=False)
    pontos = Column(Float, default=0.0)    
    
    def __init__(self, id_usuario: int, palavra: str, tentativas: int = 0, acertou: bool = False, pontos: float = 0.0): 
        self.id_usuario = id_usuario
        self.palavra = palavra
        self.tentativas = tentativas
        self.acertou = acertou
        self.pontos = pontos