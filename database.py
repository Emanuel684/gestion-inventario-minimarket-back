"""Modulo con las funciones de conexion y ejecucion de sql a la base de datos."""

# External libraries
import oracledb

from properties.settings import Settings
from functools import lru_cache


@lru_cache()
def crear_oracle_conexion() -> oracledb.connect:
    """Crea la conexion con la base de datos.

    Returns:
        Objeto de conexion con la base de datos Oracle.

    """
    settings = Settings()
    return oracledb.connect(settings.database_connection_str, events=True)


@lru_cache()
def crear_cursor_oracle(conexion):
    """Retorna el cursor sobre la base de datos para ejecutar operaciones.

    Args:
        conexion: Conexion a la base de datos.

    Returns:
        Cursor para ejecutar operaciones sobre la base de datos
    """
    return lambda: conexion.cursor()
