from models import Usuario, Livro
from database import Base, engine
from sqlalchemy.orm import Session

with Session(bind=engine) as session:
    Base.metadata.create_all(bind = engine)

    usuario = Usuario(nome= "Maria", email ="maria.com@gmail")
    livro = Livro(titulo = "Dom Casmurro", id_usuario = 1)

    session.add(usuario)
    session.add(livro)

    session.commit()