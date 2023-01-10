# Aplication for Codhab --#
# Daniel Moraes ----------#
# API - CRUD -------------#

from fastapi import FastAPI,Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models import Usuario 
from database import engine, Base, get_db
from schemas import UsuarioRequest, UsuarioResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def aplicacao_codhab():
    return {"Mensagem":"CRUD Codhab"}

#CADASTRO
@app.post("/api/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED) #Requisicoes do tipo POST // Rotas de requisicoes //<< Injecao de dependencias >>
def create(request: UsuarioRequest, db: Session = Depends(get_db)):
    usuario = UsuarioRepository.save(db, Usuario(**request.dict()))
    return UsuarioResponse.from_orm(usuario)

#LISTAGEM
@app.get("/api/usuarios",response_model=list[UsuarioResponse])
def find_all(db: Session = Depends(get_db)):
    usuarios = UsuarioRepository.find_all(db)
    return [UsuarioResponse.from_orm(usuario)for usuario in usuarios]


