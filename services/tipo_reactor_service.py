"""Modulo con los servicios correspondientes a los tipo reactores en la base
    de datos"""

# External libraries
from typing import Callable
from sqlmodel import Session

# Own libraries
from repositories.tipo_reactor_repositorie import TipoReactorRepository
from services.base_service import ServiceBase


class TipoReactorService(ServiceBase):
    def __init__(self, cursor: Callable[[], Session]) -> None:
        """Crea una nueva instancia del servicio de tipo de reactores

        Args:
            cursor: Cursor para ejecutar operaciones sobre mongo db.
        """
        self._session_factory = cursor

    def __enter__(self):
        self._session = self._session_factory()
        self.tipo_reactor_repository = TipoReactorRepository(self._session)
        return super().__enter__()
