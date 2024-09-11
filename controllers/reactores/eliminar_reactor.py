"""Modulo con el endpoint para eliminar un reactor por identificador (ID)"""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar
from services.reactor_service import ReactorService
from utilities.qx_wrap import wrapper

eliminar_reactor_controller = APIRouter(prefix='/reactores', tags=['reactores'])


@eliminar_reactor_controller.delete('/eliminar-reactor/{identificador}', status_code=200)
@wrapper
def elimina_reactor(response: Response, identificador: int) -> RespuestaEstandar:
    """Elimina un registro correspondiente a un reactor en la base de datos

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al reactor que queremos eliminar

    Returns:
        Si la informacion del reactor fue eliminado correctamente o no.

        .. code-block: python

            {
              'data': 'Reactor identificado como 1 eliminado correctamente',
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    respuesta = 'Reactor no eliminado correctamente'
    with ReactorService(cursor=cursor) as reactor_service:
        reactor_service.reactores_repository.delete(identificador)
        hero_john = reactor_service.reactores_repository.get_by_id(identificador)
        if hero_john is None:
            respuesta = (
                f'Reactor identificado como {identificador} eliminado correctamente'
            )
        reactor_service.commit()

    return respuesta
