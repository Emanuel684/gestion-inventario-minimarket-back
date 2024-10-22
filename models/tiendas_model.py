"""Modulo con los modelos de la base de datos"""

# External libraries
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

from models.base_model import RespuestaEstandar

# Representa un campo ObjectId en la base de datos.
# Se representará como una `str` en el modelo para que pueda serializarse en JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class TiendaModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    """Contiene la información generada por los endpoints."""

    id_usuario_tendero: str | int = None
    """Contiene la información generada por los endpoints."""

    nombre: str = None
    """Contiene la información generada por los endpoints."""

    ciudad: str = None
    """Contiene la información generada por los endpoints."""

    pais: str = None
    """Contiene la información generada por los endpoints."""

    direccion: str = None
    """Contiene la información generada por los endpoints."""

    telefono: str = None
    """Contiene la información generada por los endpoints."""

    celular: str = None
    """Contiene la información generada por los endpoints."""

    hora_inicio: str = None
    """Contiene la información generada por los endpoints."""

    hora_fin: str = None
    """Contiene la información generada por los endpoints."""

    fecha_creacion: str = None
    """Contiene la información generada por los endpoints."""

    fecha_actualizacion: str = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "id": "662d10f8dd91ebe8c34a81f2",
                "id_usuario_tendero": "662d10f8dd91ebe8c34a81f2",
                "nombre": "RanchoTienda",
                "ciudad": "Medellín",
                "pais": "Colombia",
                "direccion": "Carrera 65 C #47 Sur 44",
                "telefono": "4187277",
                "celular": "3187604393",
                "hora_inicio": "08:00",
                "hora_fin": "16:00",
                "fecha_creacion": "2024-10-22T00:00:00",
                "fecha_actualizacion": "2024-10-22T00:00:00",
            }
        },
    )


class UpdateTiendaModel(BaseModel):

    id_usuario_tendero: str | int = None
    """Contiene la información generada por los endpoints."""

    nombre: str = None
    """Contiene la información generada por los endpoints."""

    ciudad: str = None
    """Contiene la información generada por los endpoints."""

    pais: str = None
    """Contiene la información generada por los endpoints."""

    direccion: str = None
    """Contiene la información generada por los endpoints."""

    telefono: str = None
    """Contiene la información generada por los endpoints."""

    celular: str = None
    """Contiene la información generada por los endpoints."""

    hora_inicio: str = None
    """Contiene la información generada por los endpoints."""

    hora_fin: str = None
    """Contiene la información generada por los endpoints."""

    fecha_creacion: str = None
    """Contiene la información generada por los endpoints."""

    fecha_actualizacion: str = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True, json_encoders={ObjectId: str}
    )


class TiendasCollection(RespuestaEstandar):

    data: List[TiendaModel] | None = None
    """Contiene la información generada por los endpoints."""


class TiendaCollection(RespuestaEstandar):

    data: TiendaModel = {}
    """Contiene la información generada por los endpoints."""
