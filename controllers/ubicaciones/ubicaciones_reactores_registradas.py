"""Modulo con el endpoint para obtener todos los reactores registrados por
    ubicacion en la base de datos."""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.reactores_model import ReactoresCollection
from services.ubicacion_service import UbicacionService

ubicaciones_reactores_registradas_controller = APIRouter(
    prefix="/ubicaciones", tags=["ubicaciones"]
)


@ubicaciones_reactores_registradas_controller.get(
    "/ubicaciones-reactores-registrados/{identificador}",
    status_code=200,
    response_model=ReactoresCollection,
    response_model_by_alias=False,
)
def ubicaciones_reactores_registrados(response: Response, identificador: str):
    """Obtener todos los reactores registrados en la tabla REACTORES

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todos los reactores registrados en la base de datos

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': [
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
            }

    """
    success = None
    data = [None]
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with UbicacionService(cursor=cursor) as ubicacion_service:
            data = ubicacion_service.ubicaciones_repository.get_list_reactores(
                identificador
            )

        if data is None:
            message = f"Reactores en ubicación {identificador} no encontrados"
            status_code = 404
            data = None
            success = False
        else:
            message = "Se obtuvo el resultado exitosamente."
            success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = None
        message = f"Error al obtener el resultado {traceback.format_exc()}"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        respuesta = ReactoresCollection(success=success, msg=message, data=data)

    return respuesta
