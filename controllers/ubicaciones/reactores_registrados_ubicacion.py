"""Modulo con el endpoint para obtener todas la ubicaciones registradas en la
    base de datos"""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.ubicacion_service import UbicacionService
from utilities.qx_wrap import wrapper

reactores_registrados_ubicacion_controller = APIRouter(
    prefix='/ubicaciones', tags=['ubicaciones']
)


@reactores_registrados_ubicacion_controller.get(
    '/reactores-registrados-ubicacion', status_code=200
)
@wrapper
def reactores_registrados_ubicacion(response: Response) -> RespuestaEstandar:
    """Obtiene todas las ubicaciones registradas en la base de datos

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todas las ubicaciones registradas en la base de datos

        .. code-block: python

            {
              'data': [
                {
                  'NOMBRE_CIUDAD': 'Kinshasa',
                  'CIUDAD_ID': 1
                },
                {
                  'NOMBRE_CIUDAD': 'Algiers',
                  'CIUDAD_ID': 2
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with UbicacionService(cursor=cursor) as ubicacion_service:
        respuesta = ubicacion_service.ubicaciones_repository.list()

    return respuesta
