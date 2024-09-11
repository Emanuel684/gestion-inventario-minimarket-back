"""Modulo con los servicios correspondientes a las ubicaciones en la base de
    datos"""

# External libraries
from typing import Callable
from sqlmodel import Session

# Own libraries
from contexts.database import crear_oracle_conexion
from repositories.ubicacion_repositorie import UbicacionRepository
from services.base_service import ServiceBase


class UbicacionService(ServiceBase):
    def __init__(self, cursor: Callable[[], Session]) -> None:
        """Crea una nueva instancia del servicio de ubicaciones

        Args:
            cursor: Cursor para realizar transacciones sobre la base de datos.
        """
        self._cursor = cursor

    def __enter__(self):
        self._session = self._cursor()
        self.ubicaciones_repository = UbicacionRepository(self._session)
        return super().__enter__()

    def commit(self):
        """Commits la transaccion actual."""
        conexion = crear_oracle_conexion()
        conexion.commit()

    def rollback(self):
        """Rollbacks la transaccion actual."""
        conexion = crear_oracle_conexion()
        conexion.rollback()
