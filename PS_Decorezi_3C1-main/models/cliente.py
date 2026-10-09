from .base import ModeloBase
from . import db


class Cliente(ModeloBase):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=True)

    def cadastrar_cliente(email, senha):
        cliente = Cliente(email=email, senha=senha)
        db.session.add(cliente)
        db.session.commit()
        return cliente