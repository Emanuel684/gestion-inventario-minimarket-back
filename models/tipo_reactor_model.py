"""Modulo con configuraciones necesaria en el api"""

# External libraries
from typing import Optional
from sqlmodel import Field, Column, Integer, String
from models.base_model import BaseModel


class TipoReactor(BaseModel, table=True):
    """Tabla de TIPO_REACTORES en la base de datos."""

    __tablename__ = 'TipoReactor'

    id: Optional[int] = Field(
        sa_column=Column('Id', Integer, primary_key=True, autoincrement=True)
    )
    Nombre: str = Field(sa_column=Column('Nombre', String(30), nullable=False))
