"""Modulo con las clases correspondientes al repository de la tabla REACTORES en
    la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from pymongo import ReturnDocument
from sqlmodel import Session

from models.inventarios_model import InventarioModel


class InventarioRepository(ABC):
    """Repositorio correspondiente al manejo del inventario en la aplicación"""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un inventario segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al inventario

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_inventario': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        respuesta = self._session.inventarios.find_one({"_id": ObjectId(identificador)})
        return respuesta

    def get_list(self) -> list:
        """Obtener todos los inventarios registrados en la colleccion de Mongo Db

        Returns:
            Todos los inventarios

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c027c',
                      'nombre_inventario': 'SUR Hannover',
                      'pais': 'Germany',
                      'ciudad': 'Hannover',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0.001,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1971-12-09T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c027f',
                      'nombre_inventario': 'SUR Munich',
                      'pais': 'Germany',
                      'ciudad': 'Munich',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1962-02-01T00:00:00'
                    }
                ]

        """
        inventarios = self._session.inventarios.find({})
        respuesta = list(inventarios)
        return respuesta

    def add(self, record: InventarioModel) -> dict:
        """Crea un nuevo registro en la coreccion de inventarios

        Args:
            record (InventarioModel): informacion del inventario a agregar a la colleccion

        Returns:
            Informacion del inventario agregado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_inventario': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """

        nuevo_inventario = self._session.inventarios.insert_one(
            record.model_dump(by_alias=True, exclude=["id"])
        )
        inventario_creado = self._session.inventarios.find_one(
            {"_id": nuevo_inventario.inserted_id}
        )

        return inventario_creado

    def update(self, identificador: str, record: InventarioModel) -> dict:
        """Actualiza informacion de un inventario segun su identificador.

        Args:
            identificador (str): Identificador del inventario a actualizar informacion.
            record (InventarioModel): Informacion que se actualizara del registro.

        Returns:
            Informacion del inventario actualizado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_inventario': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        inventario = {
            clave: valor
            for clave, valor in record.model_dump(by_alias=True).items()
            if valor is not None
        }

        if len(inventario) >= 1:
            inventario_actualizado = self._session.inventarios.find_one_and_update(
                {"_id": ObjectId(identificador)},
                {"$set": inventario},
                return_document=ReturnDocument.AFTER,
            )

        return inventario_actualizado

    def delete(self, identificador: str):
        """Elimina un inventario segun su identificador en la coleccion de inventarios.

        Args:
            identificador (str): Identificador del inventario a actualizar informacion.

        Returns:
            Elementos eliminados de la colleccion.

        """
        record = self._session.inventarios.delete_one({"_id": ObjectId(identificador)})

        return record
