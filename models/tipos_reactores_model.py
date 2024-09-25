"""Modulo con los modelos de la base de datos"""

# External libraries
from typing import List, Optional

from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

from models.base_model import RespuestaEstandar

# Representa un campo ObjectId en la base de datos.
# Se representará como una `str` en el modelo para que pueda serializarse en JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class TipoReactorModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    """Contiene la información generada por los endpoints."""

    tipo: str
    """Contiene la información generada por los endpoints."""


class TiposReactoresCollection(RespuestaEstandar):

    data: List[TipoReactorModel]
    """Contiene la información generada por los endpoints."""


class TipoReactorCollection(RespuestaEstandar):

    data: TipoReactorModel
    """Contiene la información generada por los endpoints."""
