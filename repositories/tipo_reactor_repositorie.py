"""Modulo con las clases correspondientes al repository de la tabla
    TIPO_REACTORES en la base de datos."""

# External libraries
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, Optional, List
from sqlmodel import Session
from models.tipo_reactor_model import BaseModel, TipoReactor

T = TypeVar('T', bound=BaseModel)


class GenericRepository(Generic[T], ABC):
    """Generic base repository."""

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        """Get a single record by id.

        Args:
            id (int): Record id.

        Returns:
            Optional[T]: Record or none.
        """
        raise NotImplementedError()

    @abstractmethod
    def list(self, **filters) -> List[T]:
        """Gets a list of records

        Args:
            **filters: Filter conditions, several criteria are linked with a logical 'and'.

         Raises:
            ValueError: Invalid filter condition.

        Returns:
            List[T]: List of records.
        """
        raise NotImplementedError()


class TipoReactorRepository(GenericRepository[T], ABC):
    """Generic SQL Repository."""

    def __init__(self, session: Session) -> None:
        """Creates a new repository instance.

        Args:
            session (Session): SQLModel session.
        """
        self._session = session

    def get_by_id(self, id: int) -> Optional[T]:
        respuesta = self._session.execute(
            f"""SELECT r.ID ID_REACTOR, r.TIPO_REACTOR_ID, r.ESTADO_REACTOR_ID, r.CIUDAD_ID, r.NOMBRE NOMBRE_REACTOR, r.POTENCIA_TERMICA, r.FECHA_PRIMERA_REACCION,
tr.NOMBRE NOMBRE_TIPO_REACTOR FROM IAEA.REACTORES r 
INNER JOIN IAEA.TIPO_REACTORES tr ON r.TIPO_REACTOR_ID = tr.ID 
WHERE R.TIPO_REACTOR_ID = '{id}'"""
        )
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchall()
        print('respuesta: ', respuesta)

        return respuesta

    def list(self, **filters) -> List[T]:
        respuesta = self._session.execute("""SELECT * FROM IAEA.TIPO_REACTORES tr """)
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchall()

        return respuesta
