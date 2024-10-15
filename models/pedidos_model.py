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


class PedidoModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    """Contiene la información generada por los endpoints."""

    id_tienda: str | int = None
    """Contiene la información generada por los endpoints."""

    id_cliente: str = None
    """Contiene la información generada por los endpoints."""

    productos: str = None
    """Contiene la información generada por los endpoints."""

    precio_total: str = None
    """Contiene la información generada por los endpoints."""

    direccion: int | float = None
    """Contiene la información generada por los endpoints."""

    fecha_entrega: str = None
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
                "nombre_reactor": "Isis",
                "pais": "France",
                "ciudad": "Gif-sur-Yvette",
                "tipo": "POOL",
                "potencia_termica": 700,
                "estado": "UNDER DECOMMISSIONING",
                "fecha_primera_reaccion": "1966-04-28T00:00:00",
            }
        },
    )


class UpdatePedidoModel(BaseModel):

    nombre_reactor: str | int = None
    """Contiene la información generada por los endpoints."""

    pais: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    ciudad: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    tipo: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    potencia_termica: Optional[float] = None
    """Contiene la información generada por los endpoints."""

    estado: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    fecha_primera_reaccion: Optional[str] = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True, json_encoders={ObjectId: str}
    )


class PedidosCollection(RespuestaEstandar):

    data: List[PedidoModel] | None = None
    """Contiene la información generada por los endpoints."""


class PedidoCollection(RespuestaEstandar):

    data: PedidoModel = {}
    """Contiene la información generada por los endpoints."""
