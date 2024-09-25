"""Modulo con los modelos de la base de datos"""

# External libraries
from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from models.base_model import RespuestaEstandar

# Representa un campo ObjectId en la base de datos.
# Se representará como una `str` en el modelo para que pueda serializarse en JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class UbicacionModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    """Contiene la información generada por los endpoints."""

    nombre_pais: str = None
    """Contiene la información generada por los endpoints."""

    nombre_ciudad: str = None
    """Contiene la información generada por los endpoints."""


class UbicacionesCollection(RespuestaEstandar):

    data: List[UbicacionModel] | None
    """Contiene la información generada por los endpoints."""


class UbicacionCollection(RespuestaEstandar):

    data: UbicacionModel
    """Contiene la información generada por los endpoints."""
