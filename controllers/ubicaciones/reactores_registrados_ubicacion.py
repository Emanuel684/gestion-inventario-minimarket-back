"""Modulo con el endpoint para obtener todas la ubicaciones registradas en la
    base de datos"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_mongo_conexion, crear_cursor_mongo
from models.ubicaciones_model import UbicacionesCollection
from services.ubicacion_service import UbicacionService
from helpers.config import get_log

reactores_registrados_ubicacion_controller = APIRouter(
    prefix='/ubicaciones', tags=['ubicaciones']
)


@reactores_registrados_ubicacion_controller.get(
    '/reactores-registrados-ubicacion',
    status_code=200,
    response_model=UbicacionesCollection,
    response_model_by_alias=False,
)
def reactores_registrados_ubicacion(response: Response):
    """Obtiene todas las ubicaciones registradas en la base de datos

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todas las ubicaciones registradas en la base de datos

        .. code-block:: python

            {
              'data': [
                {
                  'id': '662cfec75363bbc93a0c0125',
                  'nombre_pais': 'Democratic Republic of the Congo',
                  'nombre_ciudad': 'Kinshasa'
                },
                {
                  'id': '662cfec75363bbc93a0c0126',
                  'nombre_pais': 'Algeria',
                  'nombre_ciudad': 'Algiers'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    success = None
    data = None
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with UbicacionService(cursor=cursor) as ubicacion_service:
            data = ubicacion_service.ubicaciones_repository.get_list()
        message = 'Se obtuvo el resultado exitosamente.'
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = None
        message = f'Error al obtener el resultado {traceback.format_exc()}'
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        respuesta = UbicacionesCollection(success=success, msg=message, data=data)

    return respuesta
