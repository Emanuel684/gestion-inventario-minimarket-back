"""Modulo con los modelos de la base de datos"""

# External libraries
from typing import Optional
from sqlmodel import Field, Column, Integer, String, ForeignKey
from models.base_model import BaseModel


class Reactor(BaseModel, table=True):
    """Tabla de REACTORES en la base de datos."""

    __tablename__ = 'Reactor'

    id: Optional[int] = Field(
        sa_column=Column('Id', Integer, primary_key=True, autoincrement=True)
    )
    tipo_reactor_id: int = Field(
        sa_column=Column(
            'TipoReactorId', Integer, ForeignKey('TipoReactor.Id'), nullable=False
        )
    )
    estado_reactor_id: int = Field(
        sa_column=Column(
            'EstadoReactorId', Integer, ForeignKey('EstadoReactor.Id'), nullable=False
        )
    )
    ciudad_id: int = Field(
        sa_column=Column('CiudadId', Integer, ForeignKey('Ciudad.Id'), nullable=False)
    )
    nombre: str = Field(sa_column=Column('Nombre', String(30), nullable=False))
    potencia_termica: Optional[int] = Field(
        sa_column=Column('PotenciaTermica', Integer, nullable=True, default=None)
    )
    fecha_primera_reaccion: str = Field(
        sa_column=Column('FechaPrimeraReaccion', String(30), nullable=True, default=None)
    )
