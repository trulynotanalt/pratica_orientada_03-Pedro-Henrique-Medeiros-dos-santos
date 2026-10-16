from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///biblioteca.db")

def SessionLocal():
    return Session(bind= engine)
    
