from .base import ModeloBase
from . import db


class Moveis(ModeloBase):
    __tablename__ = "moveis"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    id_moveis = db.Column(db.Integer, db.ForeignKey("moveis.id"), nullable=False)
    