"""Modulo con las clases correspondientes al repository de la tabla TIPO_REACTORES
    en la base de datos."""

# External libraries
from abc import ABC
from bson import ObjectId
from sqlmodel import Session


class TipoReactorRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los reactores."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un tipo de reactor segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al tipo de reactor

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c0425',
                      'nombre_reactor': 'PBR Plum Brook Reactor',
                      'pais': 'United States of America',
                      'ciudad': 'Sandusky, OH',
                      'tipo': 'TANK',
                      'potencia_termica': 60000,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1961-01-01T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c0553',
                      'nombre_reactor': 'HFETR',
                      'pais': 'China',
                      'ciudad': 'Chengdu',
                      'tipo': 'TANK',
                      'potencia_termica': 125000,
                      'estado': 'OPERATIONAL',
                      'fecha_primera_reaccion': '1979-12-27T00:00:00'
                    }
                ]

        """
        res_tipo_reac = self._session.tipos_reactores.find_one(
            {'_id': ObjectId(identificador)}
        )
        respuesta = self._session.reactores.find({'tipo': res_tipo_reac['tipo']})

        return respuesta

    def get_list(self) -> list:
        """Obtener todos los tipos de reactores registrados en la colleccion de
            Mongo Db

        Returns:
            Todos los tipos de reactores

            .. code-block:: python

                [
                    {
                      'id': '662cf9395363bbc93a0c00d9',
                      'tipo': 'TANK'
                    },
                    {
                      'id': '662cf9395363bbc93a0c00d6',
                      'tipo': 'HEAVY WATER'
                    }
                ]

        """
        tipos_reactores = self._session.tipos_reactores.find({})
        respuesta = list(tipos_reactores)

        return respuesta
