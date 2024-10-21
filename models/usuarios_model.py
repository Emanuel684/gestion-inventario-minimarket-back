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


class UsuarioModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    """Contiene la información generada por los endpoints."""

    nombre_completo: str | int = None
    """Contiene la información generada por los endpoints."""

    email: str | int = None
    """Contiene la información generada por los endpoints."""

    password: str | int = None
    """Contiene la información generada por los endpoints."""

    pais: str = None
    """Contiene la información generada por los endpoints."""

    ciudad: str = None
    """Contiene la información generada por los endpoints."""

    tipo: str = None
    """Contiene la información generada por los endpoints."""

    fecha_creacion: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    fecha_actualizacion: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "id": "662d0d325363bbc93a0c0295",
                "nombre_completo": "Emanuel Acevedo",
                "email": "emanuelacag@gmail.com",
                "pais": "Colombia",
                "ciudad": "Medellín",
                "tipo": "cliente",
                "fecha_creacion": "1966-04-28T00:00:00",
                "fecha_actualizacion": "1966-04-28T00:00:00",
            }
        },
    )


class UpdateUsuarioModel(BaseModel):

    nombre_completo: str | int = None
    """Contiene la información generada por los endpoints."""

    email: str | int = None
    """Contiene la información generada por los endpoints."""

    password: str = None
    """Contiene la información generada por los endpoints."""

    pais: str = None
    """Contiene la información generada por los endpoints."""

    ciudad: str = None
    """Contiene la información generada por los endpoints."""

    tipo: str = None
    """Contiene la información generada por los endpoints."""

    fecha_actualizacion: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True, json_encoders={ObjectId: str}
    )


class UsuariosCollection(RespuestaEstandar):

    data: List[UsuarioModel] | None = None
    """Contiene la información generada por los endpoints."""


class UsuarioCollection(RespuestaEstandar):

    data: UsuarioModel = {}
    """Contiene la información generada por los endpoints."""
