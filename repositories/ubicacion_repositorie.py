"""Modulo con las clases correspondientes al repository de la tabla CIUDADES
    y PAISES en la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from sqlmodel import Session


class UbicacionRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los reactores."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de una ubicacion segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente a las ubicaciones de los reactores

            .. code-block:: python

                {
                    'id': '662cfec75363bbc93a0c0125',
                    'nombre_pais': 'Democratic Republic of the Congo',
                    'nombre_ciudad': 'Kinshasa'
                }

        """
        respuesta = self._session.ubicaciones.find_one({"_id": ObjectId(identificador)})

        return respuesta

    def get_list(self) -> list:
        """Obtener todos las ubicaciones registradass en la colleccion de
            Mongo Db

        Returns:
            Todas las ubicaciones registradas

            .. code-block:: python

                [
                    {
                      'id': '662cfec75363bbc93a0c0125',
                      'nombre_pais': 'Democratic Republic of the Congo',
                      'nombre_ciudad': 'Kinshasa'
                    },
                    {
                      'id': '662cfec75363bbc93a0c0126',
                      'nombre_pais': 'Algeria',
                      'nombre_ciudad': 'Algiers'
                    }
                ]

        """
        ubicaciones = self._session.ubicaciones.find({})
        respuesta = list(ubicaciones)

        return respuesta

    def get_list_reactores(self, identificador: str) -> list:
        """Obtener todos los reactores registrados en una ubicacion en la base
            de datos de Mongo.

        Returns:
            Todos los reactores en una ubicacion registradas

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c026b',
                      'nombre_reactor': 'TRICO II',
                      'pais': 'Democratic Republic of the Congo',
                      'ciudad': 'Kinshasa',
                      'tipo': 'TRIGA MARK II',
                      'potencia_termica': 1000,
                      'estado': 'EXTENDED SHUTDOWN',
                      'fecha_primera_reaccion': '1972-03-24T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c0565',
                      'nombre_reactor': 'TRICO I',
                      'pais': 'Democratic Republic of the Congo',
                      'ciudad': 'Kinshasa',
                      'tipo': 'TRIGA MARK I',
                      'potencia_termica': 50,
                      'estado': 'PERMANENT SHUTDOWN',
                      'fecha_primera_reaccion': '1959-06-06T00:00:00'
                    }
                ]

        """
        res_ubicaciones_id = self.get_by_id(identificador)
        respuesta = self._session.reactores.find(
            {
                "pais": res_ubicaciones_id["nombre_pais"],
                "ciudad": res_ubicaciones_id["nombre_ciudad"],
            }
        )

        return respuesta
