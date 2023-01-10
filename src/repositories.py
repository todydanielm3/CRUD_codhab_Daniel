#---- Aplic for Codhab ------------
#Camada de Repositoio - Daniel Moraes -
# Meodos estaicos <><><><><><><><><><><>
#----------------------------------

from sqlalchemy.orm import Session
from models import Usuario

class UsuarioRepository:
    @staticmethod
    def find_all(db: Session) -> list[Usuario]: # Busca 
        return db.query(Usuario).all()

    @staticmethod
    def save(db: Session, usuario: Usuario)-> Usuario: # Salvar um usuario no BD // cadastrar novo // atualizar inf usuarios
        if usuario.id:
            db.merge(usuario)
        else:
            db.add(usuario)
        db.commit()
        return usuario
    
    @staticmethod
    def find_by_id(db: Session, id: int)-> Usuario:
        return db.query(Usuario).filter(Usuario.id == id).first()

    @staticmethod
    def existis_by_id(db: Session, id:int)-> bool:
        return db.query(Usuario).filter(Usuario.id == id).first() is not None


    @staticmethod
    def delete_by_id(db: Session, id: int) -> None: # Excluir Usuario
        usuario = db.query(usuario).filter(usuario.id == id).first()
        if usuario is not None:
            db.delete(usuario)
            db.commit()




