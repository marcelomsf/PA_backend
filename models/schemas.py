from pydantic import BaseModel
from typing import Optional


class UsuarioSchema(BaseModel):
    username: str
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]
    
    class Config:
        from_attributes = True
    
class JogoSchema(BaseModel):
    id_usuario : int
    palavra: str
    tentativas: int
    acerto : bool
    pontos: Optional[float]
    
    class Config:
        from_attributes = True
    

class LoginScheme(BaseModel):
    username: str
    hashed_password: str

    class Config:
        from_attributes = True