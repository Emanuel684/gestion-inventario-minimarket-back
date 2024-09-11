"""Modulo con las clases correspondientes al repository de la tabla REACTORES
    en la base de datos."""

# External libraries
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, Optional, List

from sqlmodel import Session

from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from models.reactor_model import BaseModel

T = TypeVar('T', bound=BaseModel)


class GenericRepository(Generic[T], ABC):
    """Repositorio base genérico."""

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
        print('Lista de reactores')
        raise NotImplementedError()

    @abstractmethod
    def add(self, record: T) -> T:
        """Creates a new record.

        Args:
            record (T): The record to be created.

        Returns:
            T: The created record.
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self, record: T) -> T:
        """Updates an existing record.

        Args:
            record (T): The record to be updated incl. record id.

        Returns:
            T: The updated record.
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: int) -> None:
        """Deletes a record by id.

        Args:
            id (int): Record id.
        """
        raise NotImplementedError()


class ReactorRepository(GenericRepository[T], ABC):
    """Generic SQL Repository."""

    def __init__(self, session: Session) -> None:
        """Creates a new repository instance.

        Args:
            session (Session): SQLModel session.
            model_cls (Type[T]): SQLModel class type.
        """
        print('__init__ GenericSqlRepository')
        self._session = session

    def get_by_id(self, id: int) -> Optional[T]:
        respuesta = self._session.execute(
            f"""SELECT * FROM IAEA.REACTORES R WHERE R.ID = '{id}'"""
        )
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchone()

        return respuesta

    def list(self, **filters) -> List[T]:
        respuesta = self._session.execute("""SELECT * FROM IAEA.REACTORES""")
        columns = [col[0] for col in respuesta.description]
        respuesta.rowfactory = lambda *args: dict(zip(columns, args))
        respuesta = respuesta.fetchall()

        return respuesta

    def add(self, record: T) -> T:
        """Crea un nuevo registro en la tabla de REACTORES

        Args:
            record:

        Returns:

        """
        conexion = crear_oracle_conexion()
        cursor = crear_cursor_oracle(conexion)

        update = [
            record.tipo_reactor_id,
            record.estado_reactor_id,
            record.ciudad_id,
            record.nombre,
            record.potencia_termica,
            record.fecha_primera_reaccion,
        ]
        cursor().callproc('IAEA.P_INSERTA_REACTOR', update)
        return record

    def update(self, record: T) -> T:
        """

        Args:
            record:

        Returns:

        """
        conexion = crear_oracle_conexion()
        cursor = crear_cursor_oracle(conexion)

        update = [
            record.id,
            record.tipo_reactor_id,
            record.estado_reactor_id,
            record.ciudad_id,
            record.nombre,
            record.potencia_termica,
            record.fecha_primera_reaccion,
        ]
        cursor().callproc('IAEA.P_ACTUALIZA_REACTOR', update)
        return record

    def delete(self, id: int) -> None:
        record = self.get_by_id(id)
        if record is not None:
            conexion = crear_oracle_conexion()
            cursor = crear_cursor_oracle(conexion)
            cursor().callproc('IAEA.P_ELIMINA_REACTOR', [id])
