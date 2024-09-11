"""Modulo con el modelo de la tabla de ubicaciones (CIUDADES) correspondiente
    a la base de datos"""

# External libraries
from typing import Optional
from sqlmodel import Field, Column, Integer, String
from models.base_model import BaseModel


class Pais(BaseModel, table=True):
    """Tabla de PAISES en la base de datos."""

    __tablename__ = 'Pais'

    id: Optional[int] = Field(
        sa_column=Column('Id', Integer, primary_key=True, autoincrement=True)
    )
    nombre: str = Field(sa_column=Column('Nombre', String(30), nullable=False))
