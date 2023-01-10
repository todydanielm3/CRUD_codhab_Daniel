#---- Aplic for Codhab ------------
#Criação dos Modelos - Daniel Moraes -
#----------------------------------

from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    #ID, CPF, NOME, EMAIL e TELEFONE
    id: int = Column(Integer,primary_key=True,index=True)
    cpf: int = Column(Integer,nullable=False)
    nome: str = Column(String(100),nullable=False)
    email: str = Column(String(100),nullable=False)
    telefone: int = Column(Integer,nullable=False)
