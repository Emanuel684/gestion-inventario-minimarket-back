"""Modulo con las clases correspondientes al repository de la tabla REACTORES en
    la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from pymongo import ReturnDocument
from sqlmodel import Session

from models.reactores_model import ReactorModel


class ReactorRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los reactores."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un reactor segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al reactor

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_reactor': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        respuesta = self._session.reactores.find_one({"_id": ObjectId(identificador)})
        return respuesta

    def get_list(self) -> list:
        """Obtener todos los reactores registrados en la colleccion de Mongo Db

        Returns:
            Todos los reactores

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c027c',
                      'nombre_reactor': 'SUR Hannover',
                      'pais': 'Germany',
                      'ciudad': 'Hannover',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0.001,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1971-12-09T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c027f',
                      'nombre_reactor': 'SUR Munich',
                      'pais': 'Germany',
                      'ciudad': 'Munich',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1962-02-01T00:00:00'
                    }
                ]

        """
        reactores = self._session.reactores.find({})
        respuesta = list(reactores)
        return respuesta

    def add(self, record: ReactorModel) -> dict:
        """Crea un nuevo registro en la coreccion de reactores

        Args:
            record (ReactorModel): informacion del reactor a agregar a la colleccion

        Returns:
            Informacion del reactor agregado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_reactor': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """

        nuevo_reactor = self._session.reactores.insert_one(
            record.model_dump(by_alias=True, exclude=["id"])
        )
        reactor_creado = self._session.reactores.find_one(
            {"_id": nuevo_reactor.inserted_id}
        )

        return reactor_creado

    def update(self, identificador: str, record: ReactorModel) -> dict:
        """Actualiza informacion de un reactor segun su identificador.

        Args:
            identificador (str): Identificador del reactor a actualizar informacion.
            record (ReactorModel): Informacion que se actualizara del registro.

        Returns:
            Informacion del reactor actualizado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_reactor': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        reactor = {
            clave: valor
            for clave, valor in record.model_dump(by_alias=True).items()
            if valor is not None
        }

        if len(reactor) >= 1:
            reactor_actualizado = self._session.reactores.find_one_and_update(
                {"_id": ObjectId(identificador)},
                {"$set": reactor},
                return_document=ReturnDocument.AFTER,
            )

        return reactor_actualizado

    def delete(self, identificador: str):
        """Elimina un reactor segun su identificador en la coleccion de reactores.

        Args:
            identificador (str): Identificador del reactor a actualizar informacion.

        Returns:
            Elementos eliminados de la colleccion.

        """
        record = self._session.reactores.delete_one({"_id": ObjectId(identificador)})

        return record
