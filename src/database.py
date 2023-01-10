#---- Aplic for Codhab ------------
#Config, com o BD - Daniel Moraes -
#----------------------------------

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"


engine = create_engine(#para aplicações usando SQLALCHEMY
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}#necessário para sqlite

)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 

    finally:
        db.close()
