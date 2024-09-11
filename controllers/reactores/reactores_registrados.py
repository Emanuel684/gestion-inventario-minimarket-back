"""Modulo con el endpoint para obtener todos los reactores registrados"""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.reactor_service import ReactorService
from utilities.qx_wrap import wrapper

reactores_registrados_controller = APIRouter(prefix='/reactores', tags=['reactores'])


@reactores_registrados_controller.get('/reactores-registrados', status_code=200)
@wrapper
def reactores_registrados(response: Response) -> RespuestaEstandar:
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
                  'ID': 481,
                  'TIPO_REACTOR_ID': 23,
                  'ESTADO_REACTOR_ID': 2,
                  'CIUDAD_ID': 137,
                  'NOMBRE': 'NTR General Electric',
                  'POTENCIA_TERMICA': 100,
                  'FECHA_PRIMERA_REACCION': '1957-11-15T00:00:00'
                },
                {
                  'ID': 482,
                  'TIPO_REACTOR_ID': 11,
                  'ESTADO_REACTOR_ID': 3,
                  'CIUDAD_ID': 188,
                  'NOMBRE': 'S1C Prototype',
                  'POTENCIA_TERMICA': 0,
                  'FECHA_PRIMERA_REACCION': '1959-01-01T00:00:00'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)
    with ReactorService(cursor=cursor) as reactores_service:
        respuesta = reactores_service.reactores_repository.list()

    return respuesta
