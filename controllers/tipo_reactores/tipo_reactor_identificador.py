"""Modulo con el endpoint para obtener tipo de reactor por identificador (ID).
    La respuesta incluye todos los reactores asociados al tipo."""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.tipo_reactor_service import TipoReactorService
from utilities.qx_wrap import wrapper

tipo_reactor_identificador_controller = APIRouter(
    prefix='/tipo-reactores', tags=['tipo_reactores']
)


@tipo_reactor_identificador_controller.get(
    '/tipo-reactores-identificador/{identificador}', status_code=200
)
@wrapper
def tipo_reactores_identificador(
    response: Response, identificador: int
) -> RespuestaEstandar:
    """Obtiene todos los tipo de reactor por identificador (ID). La respuesta
        incluye todos los reactores asociados al tipo.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: Identificador del tipo de reactor a consultar

    Returns:
        Todos los tipo de reactor por identificador (ID). La respuesta
            incluye todos los reactores asociados al tipo.

        .. code-block: python

            {
              'data': [
                {
                  'ID_REACTOR': 587,
                  'TIPO_REACTOR_ID': 1,
                  'ESTADO_REACTOR_ID': 2,
                  'CIUDAD_ID': 184,
                  'NOMBRE_REACTOR': 'ITU-TRR',
                  'POTENCIA_TERMICA': 250,
                  'FECHA_PRIMERA_REACCION': '1979-03-11T00:00:00',
                  'NOMBRE_TIPO_REACTOR': 'TRIGA MARK II'
                },
                {
                  'ID_REACTOR': 610,
                  'TIPO_REACTOR_ID': 1,
                  'ESTADO_REACTOR_ID': 2,
                  'CIUDAD_ID': 236,
                  'NOMBRE_REACTOR': 'TRIGA Puspati (RTP)',
                  'POTENCIA_TERMICA': 1000,
                  'FECHA_PRIMERA_REACCION': '1982-06-28T00:00:00',
                  'NOMBRE_TIPO_REACTOR': 'TRIGA MARK II'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with TipoReactorService(cursor=cursor) as tipo_reactor_service:
        response = tipo_reactor_service.tipo_reactor_repository.get_by_id(identificador)

    return response
