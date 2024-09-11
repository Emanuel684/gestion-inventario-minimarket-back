"""Modulo con las clases correspondientes al repository de la tabla
    CIUDADES Y PAISES en la base de datos."""

# External libraries
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from sqlmodel import Session
from models.ciudad_model import BaseModel

T = TypeVar('T', bound=BaseModel)


class UbicacionRepository(ABC):
    """Generic SQL Repository."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio.

        Args:
            session: SQLModel session.
        """
        self._session = session

    def get_by_id(self, id: int) -> Optional[T]:
        """
        Args:
            id:

        Returns:

        """
        respuesta = self._session.execute(
            f"""SELECT c.NOMBRE NOMBRE_CIUDAD, c.ID CIUDAD_ID, 
                p.NOMBRE NOMBRE_PAIS, p.ID PAIS_ID FROM IAEA.CIUDADES c 
            INNER JOIN IAEA.PAISES p ON p.ID = c.PAIS_ID 
            WHERE c.ID = {id}"""
        )
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchone()
        print('respuesta: ', respuesta)

        return respuesta

    def list(self, **filters) -> List[T]:
        """
        Args:
            **filters:

        Returns:

        """
        respuesta = self._session.execute(
            """SELECT c.NOMBRE NOMBRE_CIUDAD, c.ID CIUDAD_ID FROM IAEA.CIUDADES c """
        )
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchall()

        return respuesta

    def list_reactores(self, id: int):
        """
        Args:
            id:

        Returns:

        """
        respuesta = self._session.execute(
            f"""SELECT c.NOMBRE NOMBRE_CIUDAD, c.ID CIUDAD_ID, 
                    p.NOMBRE NOMBRE_PAIS, p.ID PAIS_ID, r.ID ID_REACTOR, 
                    r.TIPO_REACTOR_ID, r.ESTADO_REACTOR_ID, r.CIUDAD_ID, 
                    r.NOMBRE NOMBRE_REACTOR, r.POTENCIA_TERMICA, 
                    r.FECHA_PRIMERA_REACCION
                FROM IAEA.REACTORES r
                INNER JOIN IAEA.CIUDADES c ON c.ID = r.CIUDAD_ID 
                INNER JOIN IAEA.PAISES p ON p.ID = c.PAIS_ID 
                WHERE c.ID = {id}"""
        )
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchall()

        return respuesta
