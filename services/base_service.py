"""Modulo con la clase base de todos los servicios."""

# External libraries
from abc import ABC

# Own libraries
from contexts.database import crear_mongo_conexion


class ServiceBase(ABC):
    """Base de los servicios"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        conexion = crear_mongo_conexion()
        conexion.close()
