from typing import Optional
from pydantic import BaseModel, EmailStr

#propriedades exigidas durante a criação do usuário

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str