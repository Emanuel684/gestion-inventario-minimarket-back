"""Módulo con parser de estructura de datos utilizados en el director."""

# External libraries
from typing import Any
from pydantic import BaseModel


class RespuestaEstandar(BaseModel):
    """Clase que representa las respuestas estándar que tiene la API."""

    data: Any
    """Contiene la información generada por los endpoints."""

    msg: str
    """Mensaje con información sobre la ejecución del endpoint."""

    success: bool
    """Indica si la ejecución del endpoint fue exitosa."""


class Reactor(BaseModel):
    """Clase que representa a la informacion de un reactor."""

    tipo_reactor_id: int
    """Identificador del tipo de reeactor."""

    estado_reactor_id: str
    """Identificador correspondiente estado del reactor."""

    ciudad_id: int
    """Identificador de la ciudad donde se encuentra el reactor."""

    nombre: str
    """Nombre del reactor."""

    potencia_termica: int
    """Potencia termina del reactor."""

    fecha_primera_reaccion: str
    """Fecha de la primera reaccion del reactor."""


class ReactorID(Reactor):
    """Clase que representa a la informacion de la tabla REACTORES."""

    id: int
    """Identificador en la base de datos correspondiente al reactor"""
