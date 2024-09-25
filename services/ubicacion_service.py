"""Modulo con los servicios correspondientes a las ubicaciones en la base de
    datos"""

# External libraries
from typing import Callable
from sqlmodel import Session

# Own libraries
from repositories.ubicacion_repositorie import UbicacionRepository
from services.base_service import ServiceBase


class UbicacionService(ServiceBase):
    def __init__(self, cursor: Callable[[], Session]) -> None:
        """Crea una nueva instancia del servicio de ubicaciones

        Args:
            cursor: Cursor para ejecutar operaciones sobre mongo db.
        """
        self._cursor = cursor

    def __enter__(self):
        self._session = self._cursor()
        self.ubicaciones_repository = UbicacionRepository(self._session)
        return super().__enter__()
