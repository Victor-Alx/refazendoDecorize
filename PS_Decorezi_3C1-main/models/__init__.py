from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .base import ModeloBase
from .cliente import Cliente
from .fotos import Fotos
from .modelo_moveis import ModeloMoveis
from .projeto import Projeto
from .moveis import Moveis


__all__ = ["db", "ModeloBase", "Cliente", "Fotos", "ModeloMoveis", "Projeto", "Moveis"]