#---- Aplic for Codhab --------------------------------------------------------
#Camada de schemas - Daniel Moraes
#Representacao dos dados recebidos e lancados em requisicoes ou retornos HTTP.
# Para criacao dessas classes vou utilizar a lib PYDANTIC padrao do fastapi.
#------------------------------------------------------------------------------

from pydantic import BaseModel

class UsuarioBase(BaseModel):
# CPF, NOME, EMAIL e TELEFONE
    cpf: int
    nome: str
    email: str
    telefone: int


class UsuarioRequest(UsuarioBase): #recebimentos das requisicoes HTTP
    ...

class UsuarioResponse(UsuarioBase):
    id: int 

    class Config:
        orm_mode = True

# A classe UsuarioBase vai herdar os modelos e ---->  das demais **

