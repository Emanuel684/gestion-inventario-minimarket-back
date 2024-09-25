"""Modulo con los modelos de la base de datos"""

# External libraries
from typing import Optional, List
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
from models.base_model import RespuestaEstandar

# Representa un campo ObjectId en la base de datos.
# Se representará como una `str` en el modelo para que pueda serializarse en JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class InventarioModel(BaseModel):

    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    """Contiene la información generada por los endpoints."""

    nombre_reactor: str | int = None
    """Contiene la información generada por los endpoints."""

    pais: str = None
    """Contiene la información generada por los endpoints."""

    ciudad: str = None
    """Contiene la información generada por los endpoints."""

    tipo: str = None
    """Contiene la información generada por los endpoints."""

    potencia_termica: int | float = None
    """Contiene la información generada por los endpoints."""

    estado: str = None
    """Contiene la información generada por los endpoints."""

    fecha_primera_reaccion: str = None
    """Contiene la información generada por los endpoints."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            'example': {
                'id': '662d0d325363bbc93a0c0295',
                'nombre_reactor': 'Isis',
                'pais': 'France',
                'ciudad': 'Gif-sur-Yvette',
                'tipo': 'POOL',
                'potencia_termica': 700,
                'estado': 'UNDER DECOMMISSIONING',
                'fecha_primera_reaccion': '1966-04-28T00:00:00',
            }
        },
    )


class UpdateInventarioModel(BaseModel):

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
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )


class ReactoresCollection(RespuestaEstandar):

    data: List[InventarioModel] | None = None
    """Contiene la información generada por los endpoints."""


class ReactorCollection(RespuestaEstandar):

    data: InventarioModel = {}
    """Contiene la información generada por los endpoints."""
