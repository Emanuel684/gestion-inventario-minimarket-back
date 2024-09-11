"""Modulo con el endpoint para obtener ubicacion por identificador"""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.ubicacion_service import UbicacionService
from utilities.qx_wrap import wrapper

ubicacion_reactor_identificador_controller = APIRouter(
    prefix='/ubicaciones', tags=['ubicaciones']
)


@ubicacion_reactor_identificador_controller.get(
    '/ubicacion-reactor-identificador/{identificador}', status_code=200
)
@wrapper
def ubicacion_reactor_identificador(
    response: Response, identificador: int
) -> RespuestaEstandar:
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
              'data': {
                'NOMBRE_CIUDAD': 'Kinshasa',
                'CIUDAD_ID': 1,
                'NOMBRE_PAIS': 'Democratic Republic of the Congo',
                'PAIS_ID': 1
              },
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }
    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with UbicacionService(cursor=cursor) as ubicacion_service:
        respuesta = ubicacion_service.ubicaciones_repository.get_by_id(identificador)

    return respuesta
