from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


db = create_engine("sqlite:///database/test.db", connect_args={"check_same_thread": False})



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

class Palavra(Base):
    __tablename__ = 'palavras'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    palavra = Column(String, unique=True, index=True, nullable=False)
    data = Column(DateTime, nullable=False)
    
def __init__(self, palavra: str, data: DateTime):
        self.palavra = palavra
        self.data = data
        

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True , nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    
    def __init__(self, username: str, name: str, email: str, hashed_password: str, is_active: bool = True, is_admin: bool = False):
        self.username = username
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.is_admin = is_admin