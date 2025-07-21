from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

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