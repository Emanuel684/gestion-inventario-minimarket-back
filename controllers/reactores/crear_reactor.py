"""Modulo con el endpoint para crear un reactor y la informacion asociado a este"""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar, Reactor
from services.reactor_service import ReactorService
from utilities.qx_wrap import wrapper

crear_reactor_controller = APIRouter(prefix='/reactores', tags=['reactores'])


@crear_reactor_controller.post('/crear-reactor', status_code=200)
@wrapper
def crear_reactor(response: Response, reactor: Reactor) -> RespuestaEstandar:
    """Crea un reactor dada la informacion correspondiente al mismo.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        reactor: Informacion del reactor a crear en la base de datos

    Returns:
        Si el reactor fue creado exitosamente o no.

        .. code-block: python

            {
              'data': 'Reactor creado axitosamente',
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    respuesta = 'No fue posible crear el reactor'
    with ReactorService(cursor=cursor) as reactor_service:
        # uow.heroes.add(Hero(name='John Wick', secret_name='John Wick', team_id=team.id))
        reactor_service.reactores_repository.add(reactor)
        reactor_service.commit()

        respuesta = 'Reactor creado axitosamente'

    return respuesta
