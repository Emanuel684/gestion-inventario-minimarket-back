"""Modulo con las clases correspondientes al repository de la tabla REACTORES en
    la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from pymongo import ReturnDocument
from sqlmodel import Session

from models.pedidos_model import PedidoModel


class PedidoRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los pedidos."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un pedido segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al pedido

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_pedido': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        respuesta = self._session.pedidos.find_one({"_id": ObjectId(identificador)})
        return respuesta

    def get_list(self) -> list:
        """Obtener todos los pedidos registrados en la colleccion de Mongo Db

        Returns:
            Todos los pedidos

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c027c',
                      'nombre_pedido': 'SUR Hannover',
                      'pais': 'Germany',
                      'ciudad': 'Hannover',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0.001,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1971-12-09T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c027f',
                      'nombre_pedido': 'SUR Munich',
                      'pais': 'Germany',
                      'ciudad': 'Munich',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1962-02-01T00:00:00'
                    }
                ]

        """
        pedidos = self._session.pedidos.find({})
        respuesta = list(pedidos)
        return respuesta

    def add(self, record: PedidoModel) -> dict:
        """Crea un nuevo registro en la coreccion de pedidos

        Args:
            record (PedidoModel): informacion del pedido a agregar a la colleccion

        Returns:
            Informacion del pedido agregado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_pedido': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """

        nuevo_pedido = self._session.pedidos.insert_one(
            record.model_dump(by_alias=True, exclude=["id"])
        )
        pedido_creado = self._session.pedidos.find_one(
            {"_id": nuevo_pedido.inserted_id}
        )

        return pedido_creado

    def update(self, identificador: str, record: PedidoModel) -> dict:
        """Actualiza informacion de un pedido segun su identificador.

        Args:
            identificador (str): Identificador del pedido a actualizar informacion.
            record (PedidoModel): Informacion que se actualizara del registro.

        Returns:
            Informacion del pedido actualizado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_pedido': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        pedido = {
            clave: valor
            for clave, valor in record.model_dump(by_alias=True).items()
            if valor is not None
        }

        if len(pedido) >= 1:
            pedido_actualizado = self._session.pedidos.find_one_and_update(
                {"_id": ObjectId(identificador)},
                {"$set": pedido},
                return_document=ReturnDocument.AFTER,
            )

        return pedido_actualizado

    def delete(self, identificador: str):
        """Elimina un pedido segun su identificador en la coleccion de pedidos.

        Args:
            identificador (str): Identificador del pedido a actualizar informacion.

        Returns:
            Elementos eliminados de la colleccion.

        """
        record = self._session.pedidos.delete_one({"_id": ObjectId(identificador)})

        return record
