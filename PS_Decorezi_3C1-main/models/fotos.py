from .base import ModeloBase
from . import db


class Fotos(ModeloBase):
    __tablename__ = "fotos"

    id = db.Column(db.Integer, primary_key=True)
    url_imagem = db.Column(db.String(200), nullable=False)
    id_projeto = db.Column(db.Integer, db.ForeignKey("projetos.id"), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)

    