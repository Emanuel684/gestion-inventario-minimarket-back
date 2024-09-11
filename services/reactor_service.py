"""Modulo con los servicios correspondientes a los reactores en la base de datos"""

# External libraries
from typing import Callable
from sqlmodel import Session

# Own libraries
from contexts.database import crear_oracle_conexion
from repositories.reactor_repositorie import ReactorRepository
from services.base_service import ServiceBase


class ReactorService(ServiceBase):
    def __init__(self, cursor: Callable[[], Session]) -> None:
        """Crea una nueva instancia del servicio de reactores

        Args:
            cursor: Cursor para ejecutar operaciones sobre la base de datos.
        """
        self._cursor = cursor

    def __enter__(self):
        self._cursor = self._cursor()
        self.reactores_repository = ReactorRepository(self._cursor)
        return super().__enter__()

    def commit(self):
        conexion = crear_oracle_conexion()
        conexion.commit()

    def rollback(self):
        conexion = crear_oracle_conexion()
        conexion.rollback()
