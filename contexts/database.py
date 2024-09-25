"""Modulo con las funciones de conexion y ejecucion de sql a la base de datos."""

# External libraries
from properties.settings import Settings
from functools import lru_cache
from pymongo import MongoClient


def crear_mongo_conexion() -> MongoClient:
    """Crea la conexion con la base de datos.

    Returns:
        Objeto de conexion con la base de datos Oracle.

    """
    setting = Settings()

    client = MongoClient(setting.database_connection_str)
    return client


@lru_cache()
def crear_cursor_mongo(conexion: MongoClient):
    """Retorna el cursor sobre la base de datos para ejecutar operaciones.

    Args:
        conexion: Conexion a la base de datos.

    Returns:
        Cursor para ejecutar operaciones sobre la base de datos
    """
    mongo_db = conexion.iaea_reactores
    return lambda: mongo_db