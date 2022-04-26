from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

#propriedades exigidas durante a criação do usuário
#aqui é feita a validação dos dados


#função para validar os dados no momento da criação
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


#função para restringir os dados que serão mostrados na resposta
class ShowUser(BaseModel):
    username : str
    email : EmailStr
    is_active : bool

    class Config(): # diz pro pydantic converter até objetos não dicts para json
        orm_mode = True
