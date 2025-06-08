from .database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin


class Bibliotecario(UserMixin,db.Model):

    __tablename__ = 'bibliotecario'

    id_bibliotecario: Mapped[int]=  mapped_column(primary_key=True)
    cpf: Mapped[str]= mapped_column (nullable=False, unique=True)
    nome:Mapped[str] = mapped_column (nullable=False)
    endereco: Mapped[str] = mapped_column (nullable=False)
    telefone: Mapped[str]  = mapped_column ()
    senha: Mapped[str] = mapped_column(nullable=False)

  
    def get_id(self): 
        return self.id_bibliotecario


class Usuario(UserMixin,db.Model): 
    id_usuario:Mapped[int] = mapped_column(primary_key=True)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    num_emprestimos: Mapped[int] = mapped_column(default=0,nullable=False)
    endereco: Mapped[str] = mapped_column(nullable=False)
    telefone: Mapped[str] = mapped_column()
    id_categoria:Mapped[int] = mapped_column(nullable=False, default=1)
    senha: Mapped[int] =  mapped_column(nullable= False)


# class Assistente(db.Model):

#   __tablename__ = 'assistente'

#   id_assistente: Mapped[int]=  mapped_column(primary_key=True)
#   id_bibliotecario: Mapped[int]= mapped_column(ForeignKey("bibliotecario.id"))    
#   nome:Mapped[str] = mapped_column (nullable=False)
#   endereco: Mapped[str] = mapped_column (nullable=False)
#   telefone: Mapped[str] = mapped_column()
#   senha: Mapped[str] = mapped_column(nullable=False)



