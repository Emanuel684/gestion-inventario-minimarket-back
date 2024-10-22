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


class InventarioModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    """Contiene la información generada por los endpoints."""

    id_producto: str = None
    """Contiene la información generada por los endpoints."""

    id_tienda: str = None
    """Contiene la información generada por los endpoints."""

    cantidad_disponibles: str = None
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
                "id": "662d0d325363bbc93a0c0295",
                "id_producto": "662d0d325363bbc93a0c0295",
                "id_tienda": "662d0d325363bbc93a0c0295",
                "cantidad_disponibles": "700",
                "fecha_creacion": "2024-10-22T00:00:00",
                "fecha_actualizacion": "2024-10-22T00:00:00",
            }
        },
    )


class UpdateInventarioModel(BaseModel):

    id_producto: str | int = None
    """Contiene la información generada por los endpoints."""

    id_tienda: str = None
    """Contiene la información generada por los endpoints."""

    cantidad_disponibles: str = None
    """Contiene la información generada por los endpoints."""

    fecha_actualizacion: str = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True, json_encoders={ObjectId: str}
    )


class InventariosCollection(RespuestaEstandar):

    data: List[InventarioModel] | None = None
    """Contiene la información generada por los endpoints."""


class InventarioCollection(RespuestaEstandar):

    data: InventarioModel = {}
    """Contiene la información generada por los endpoints."""
