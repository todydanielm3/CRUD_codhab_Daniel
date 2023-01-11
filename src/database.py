#---- Aplic for Codhab ------------
#Config, com o BD - Daniel Moraes -
#----------------------------------
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://danielmoraes:1234@localhost/bd_postgress"

#SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///db.sqlite3"
#SQLALCHEMY_DATABASE_URL = "postgresql:///postgres:1234@localhost/tcp/bd_postgress" #via Docker
#SQLALCHEMY_DATABASE_URL ="postgresql:///postgres:1234@localhost:7777/bd_postgress"




engine = create_engine(#para aplicações usando SQLALCHEMY
    #SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}#necessário para sqlite
    
    #SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" #postgresql

    SQLALCHEMY_DATABASE_URL #DOCKER

)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 

    finally:
        db.close()
