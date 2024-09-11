"""Modulo con los servicios correspondientes a los tipo reactores en la base
    de datos"""

# External libraries
from typing import Callable
from sqlmodel import Session

# Own libraries
from contexts.database import crear_oracle_conexion
from repositories.tipo_reactor_repositorie import TipoReactorRepository
from services.base_service import ServiceBase


class TipoReactorService(ServiceBase):
    def __init__(self, cursor: Callable[[], Session]) -> None:
        """Creates a new uow instance.

        Args:
            cursor: Cursor para ejecutar operaciones sobre la base de datos.
        """
        self._session_factory = cursor

    def __enter__(self):
        self._session = self._session_factory()
        self.tipo_reactor_repository = TipoReactorRepository(self._session)
        return super().__enter__()

    def commit(self):
        """Commits la transaccion actual."""
        conexion = crear_oracle_conexion()
        conexion.commit()

    def rollback(self):
        """Rollbacks la transaccion actual."""
        conexion = crear_oracle_conexion()
        conexion.rollback()
