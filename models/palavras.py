from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Palavra(Base):
    __tablename__ = 'palavras'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    palavra = Column(String, unique=True, index=True, nullable=False)
    data = Column(DateTime, nullable=False)
    
def __init__(self, palavra: str, data: DateTime):
        self.palavra = palavra
        self.data = data