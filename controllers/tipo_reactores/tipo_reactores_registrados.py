"""Modulo con el endpoint para obtener todos los tipo de reactores registrados
    en la base de datos."""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.tipo_reactor_service import TipoReactorService
from utilities.qx_wrap import wrapper

tipo_reactores_registrados_controller = APIRouter(
    prefix='/tipo-reactores', tags=['tipo_reactores']
)


@tipo_reactores_registrados_controller.get('/tipo-reactores-registrados', status_code=200)
@wrapper
def tipo_reactores_registrados(response: Response) -> RespuestaEstandar:
    """Obtiene todos los tipo de reactores registrados en la base de datos.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todos los tipo de reactores registrados en la base de datos.

        .. code-block: python

            {
              'data': [
                {
                  'ID': 1,
                  'NOMBRE': 'TRIGA MARK II'
                },
                {
                  'ID': 2,
                  'NOMBRE': 'POOL'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }


    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with TipoReactorService(cursor=cursor) as tipo_reactor_service:
        respuesta = tipo_reactor_service.tipo_reactor_repository.list()

    return respuesta
