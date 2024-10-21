"""Modulo con las clases correspondientes al repository de la tabla usuarios en
    la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from pymongo import ReturnDocument
from sqlmodel import Session

from models.usuarios_model import UsuarioModel


class UsuarioRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los usuarios."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un usuario segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al usuario

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_usuario': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        # respuesta = self._session.usuarios.find_one({"_id": ObjectId(identificador)})
        respuesta = self._session.usuarios.find_one({"email": identificador})
        return respuesta

    def get_list(self) -> list:
        """Obtener todos los usuarios registrados en la colleccion de Mongo Db

        Returns:
            Todos los usuarios

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c027c',
                      'nombre_usuario': 'SUR Hannover',
                      'pais': 'Germany',
                      'ciudad': 'Hannover',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0.001,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1971-12-09T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c027f',
                      'nombre_usuario': 'SUR Munich',
                      'pais': 'Germany',
                      'ciudad': 'Munich',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1962-02-01T00:00:00'
                    }
                ]

        """
        usuarios = self._session.usuarios.find({})
        respuesta = list(usuarios)
        return respuesta

    def add(self, record: UsuarioModel) -> dict:
        """Crea un nuevo registro en la coreccion de usuarios

        Args:
            record (UsuarioModel): informacion del usuario a agregar a la colleccion

        Returns:
            Informacion del usuario agregado

            .. code-block:: python

                {
                    '_id': ObjectId('670555dceb7cebdfcf1ba320'),
                    'nombre_completo': 'Emanuel Acevedo',
                    'email': 'emanuelacag@gmail.com',
                    'password': '1000306848',
                    'pais': 'Colombia',
                    'ciudad': 'Medellín',
                    'tipo': 'cliente',
                    'fecha_creacion': '1966-04-28T00:00:00',
                    'fecha_actualizacion': '1966-04-28T00:00:00'
                }

        """

        nuevo_usuario = self._session.usuarios.insert_one(
            record.model_dump(by_alias=True, exclude=["id"])
        )
        usuario_creado = self._session.usuarios.find_one(
            {"_id": nuevo_usuario.inserted_id}
        )

        return usuario_creado

    def update(self, identificador: str, record: UsuarioModel) -> dict:
        """Actualiza informacion de un usuario segun su identificador.

        Args:
            identificador (str): Identificador del usuario a actualizar informacion.
            record (UsuarioModel): Informacion que se actualizara del registro.

        Returns:
            Informacion del usuario actualizado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_usuario': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        usuario = {
            clave: valor
            for clave, valor in record.model_dump(by_alias=True).items()
            if valor is not None
        }

        if len(usuario) >= 1:
            usuario_actualizado = self._session.usuarios.find_one_and_update(
                {"_id": ObjectId(identificador)},
                {"$set": usuario},
                return_document=ReturnDocument.AFTER,
            )

        return usuario_actualizado

    def delete(self, identificador: str):
        """Elimina un usuario segun su identificador en la coleccion de usuarios.

        Args:
            identificador (str): Identificador del usuario a actualizar informacion.

        Returns:
            Elementos eliminados de la colleccion.

        """
        record = self._session.usuarios.delete_one({"_id": ObjectId(identificador)})

        return record
