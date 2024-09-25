"""Modulo con los modelos de la base de datos"""

# External libraries
from pydantic import BaseModel


class RespuestaEstandar(BaseModel):
    """Clase que representa las respuestas estándar que tiene la API."""

    msg: str
    """Mensaje con información sobre la ejecución del endpoint."""

    success: bool
    """Indica si la ejecución del endpoint fue exitosa."""
