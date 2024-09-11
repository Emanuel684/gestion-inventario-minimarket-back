"""Modulo con el endpoint para obtener un reactor por identificador (ID)"""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.reactor_service import ReactorService
from utilities.qx_wrap import wrapper

reactor_identificador_controller = APIRouter(prefix='/reactores', tags=['reactores'])


@reactor_identificador_controller.get(
    '/reactor-identificador/{identificador}', status_code=200
)
@wrapper
def reactor_identificador(response: Response, identificador: int) -> RespuestaEstandar:
    """Obtener informacion de un reactor registrado en la tabla REACTORES
        segun su ID.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al reactor que queremos consultar

    Returns:
        Información corespondiente al reactor que queremos consultar.

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
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with ReactorService(cursor=cursor) as reactor_service:
        respuesta = reactor_service.reactores_repository.get_by_id(identificador)
        if respuesta is None:
            respuesta = 'No encontramos un registro con el identificador.'

    return respuesta
