from .base import ModeloBase
from . import db


class Projeto(ModeloBase):
    __tablename__ = "projetos"


    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    url_imagens = db.Column(db.String(200), nullable=True)