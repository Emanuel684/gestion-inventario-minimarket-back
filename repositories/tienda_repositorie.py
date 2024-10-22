"""Modulo con las clases correspondientes al repository de la tabla REACTORES en
    la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from pymongo import ReturnDocument
from sqlmodel import Session

from models.tiendas_model import TiendaModel


class TiendaRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los tiendas."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un tienda segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al tienda

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_tienda': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        return self._session.tiendas.find_one({"id_usuario_tendero": identificador})

    def get_list(self) -> list:
        """Obtener todos los tiendas registrados en la colleccion de Mongo Db

        Returns:
            Todos los tiendas

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c027c',
                      'nombre_tienda': 'SUR Hannover',
                      'pais': 'Germany',
                      'ciudad': 'Hannover',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0.001,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1971-12-09T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c027f',
                      'nombre_tienda': 'SUR Munich',
                      'pais': 'Germany',
                      'ciudad': 'Munich',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1962-02-01T00:00:00'
                    }
                ]

        """
        tiendas = self._session.tiendas.find({})
        respuesta = list(tiendas)
        return respuesta

    def add(self, record: TiendaModel) -> dict:
        """Crea un nuevo registro en la coreccion de tiendas

        Args:
            record (TiendaModel): informacion del tienda a agregar a la colleccion

        Returns:
            Informacion del tienda agregado

            .. code-block:: python

                {
                    '_id': '6717c1c92939b490da5fe9b0',
                    'id_usuario_tendero': '6717c09a4f00c9c785619f29',
                    'nombre': 'RanchoTienda',
                    'ciudad': 'Medellín',
                    'pais': 'Colombia',
                    'direccion': 'Carrera 65 C #47 Sur 44',
                    'telefono': '4187277',
                    'celular': '3187604393',
                    'hora_inicio': '08:00',
                    'hora_fin': '16:00',
                    'fecha_creacion': '2024-10-22T00:00:00',
                    'fecha_actualizacion': '2024-10-22T00:00:00'
                }

        """

        nueva_tienda = self._session.tiendas.insert_one(
            record.model_dump(by_alias=True, exclude=["id"])
        )
        tienda_creado = self._session.tiendas.find_one(
            {"_id": nueva_tienda.inserted_id}
        )

        return tienda_creado

    def update(self, identificador: str, record: TiendaModel) -> dict:
        """Actualiza informacion de un tienda segun su identificador.

        Args:
            identificador (str): Identificador del tienda a actualizar informacion.
            record (TiendaModel): Informacion que se actualizara del registro.

        Returns:
            Informacion del tienda actualizado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_tienda': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        tienda = {
            clave: valor
            for clave, valor in record.model_dump(by_alias=True).items()
            if valor is not None
        }

        if len(tienda) >= 1:
            tienda_actualizado = self._session.tiendas.find_one_and_update(
                {"_id": ObjectId(identificador)},
                {"$set": tienda},
                return_document=ReturnDocument.AFTER,
            )

        return tienda_actualizado

    def delete(self, identificador: str):
        """Elimina un tienda segun su identificador en la coleccion de tiendas.

        Args:
            identificador (str): Identificador del tienda a actualizar informacion.

        Returns:
            Elementos eliminados de la colleccion.

        """
        record = self._session.tiendas.delete_one({"_id": ObjectId(identificador)})

        return record
