"""Modulo con el modelo de la tabla de ubicaciones (CIUDADES) correspondiente
    a la base de datos"""

# External libraries
from typing import Optional
from sqlmodel import Field, Column, Integer, String, ForeignKey
from models.base_model import BaseModel


class Ciudad(BaseModel, table=True):
    """Tabla de CIUDADES en la base de datos."""

    __tablename__ = 'Ciudad'

    id: Optional[int] = Field(
        sa_column=Column('Id', Integer, primary_key=True, autoincrement=True)
    )
    nombre: str = Field(sa_column=Column('Nombre', String(30), nullable=False))
    pais_id: Optional[int] = Field(
        sa_column=Column('PaisId', Integer, ForeignKey('Pais.Id'))
    )
