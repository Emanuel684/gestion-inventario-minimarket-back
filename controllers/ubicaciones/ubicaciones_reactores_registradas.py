"""Modulo con el endpoint para obtener todos los reactores registrados por
    ubicacion en la base de datos."""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.ubicacion_service import UbicacionService
from utilities.qx_wrap import wrapper

ubicaciones_reactores_registradas_controller = APIRouter(
    prefix='/ubicaciones', tags=['ubicaciones']
)


@ubicaciones_reactores_registradas_controller.get(
    '/ubicaciones-reactores-registrados/{identificador}', status_code=200
)
@wrapper
def ubicaciones_reactores_registrados(
    response: Response, identificador: int
) -> RespuestaEstandar:
    """Obtener todos los reactores registrados en la tabla REACTORES

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todos los reactores registrados en la base de datos

        .. code-block: python

            {
              'data': [
                {
                  'NOMBRE_CIUDAD': 'Kinshasa',
                  'CIUDAD_ID': 1,
                  'NOMBRE_PAIS': 'Democratic Republic of the Congo',
                  'PAIS_ID': 1,
                  'ID_REACTOR': 765,
                  'TIPO_REACTOR_ID': 9,
                  'ESTADO_REACTOR_ID': 7,
                  'NOMBRE_REACTOR': 'TRICO I',
                  'POTENCIA_TERMICA': 50,
                  'FECHA_PRIMERA_REACCION': '1959-06-06T00:00:00'
                },
                {
                  'NOMBRE_CIUDAD': 'Kinshasa',
                  'CIUDAD_ID': 1,
                  'NOMBRE_PAIS': 'Democratic Republic of the Congo',
                  'PAIS_ID': 1,
                  'ID_REACTOR': 13,
                  'TIPO_REACTOR_ID': 1,
                  'ESTADO_REACTOR_ID': 1,
                  'NOMBRE_REACTOR': 'sag',
                  'POTENCIA_TERMICA': 123,
                  'FECHA_PRIMERA_REACCION': '1963-01-01T00:00:00'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with UbicacionService(cursor=cursor) as ubicacion_service:
        respuesta = ubicacion_service.ubicaciones_repository.list_reactores(identificador)

    return respuesta
