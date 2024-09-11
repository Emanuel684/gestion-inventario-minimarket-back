"""Modulo con el endpoint para actualiza un reactor y la informacion asociado a este
    segun su identificador."""

# External libraries
from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_oracle_conexion, crear_cursor_oracle
from helpers.registro_parser import RespuestaEstandar, ReactorID
from services.reactor_service import ReactorService
from utilities.qx_wrap import wrapper

actualizar_reactor_controller = APIRouter(prefix='/reactores', tags=['reactores'])


@actualizar_reactor_controller.put('/actualizar-reactor', status_code=200)
@wrapper
def actualizar_reactor(response: Response, reactor: ReactorID) -> RespuestaEstandar:
    """Actualiza la informacion correspondiente a un reactor en la base de datos.

    Returns:
        Si la informacion del reactor fue actualizada correctamente o no.

        .. code-block: python

            {
              'data': 'Reactor actualizado correctamente',
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """
    conexion = crear_oracle_conexion()
    cursor = crear_cursor_oracle(conexion)

    with ReactorService(cursor=cursor) as reactor_service:
        respuesta = reactor_service.reactores_repository.get_by_id(reactor.id)
        if respuesta is not None:
            reactor_service.reactores_repository.update(reactor)
            reactor_service.commit()
            respuesta = 'Reactor actualizado correctamente'
        else:
            respuesta = 'El reactor ya existe'

    return respuesta
