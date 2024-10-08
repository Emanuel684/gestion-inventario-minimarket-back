"""Modulo con el endpoint para actualiza un reactor y la informacion asociado a este
    segun su identificador."""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.usuarios_model import (UpdateUsuarioModel, UsuarioCollection,
                                   UsuarioModel)
from services.usuario_service import UsuarioService

recuperar_cuenta_controller = APIRouter(prefix="/usuarios", tags=["usuarios"])


@recuperar_cuenta_controller.put(
    "/recuperar-cuenta/{identificador}",
    status_code=200,
    response_model=UsuarioCollection,
    response_model_by_alias=False,
)
def recuperar_cuenta(
    response: Response, identificador: str, reactor: UpdateUsuarioModel
):
    """Actualiza la informacion correspondiente a un reactor en la base de datos.

    Returns:
        Si la informacion del reactor fue actualizada correctamente o no.

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '6632967e003a94e8c87d5658',
                'nombre_reactor': 'Isis PRUEBA ACTUALIZACION',
                'pais': 'France',
                'ciudad': 'Gif-sur-Yvette',
                'tipo': 'POOL',
                'potencia_termica': 700,
                'estado': 'UNDER DECOMMISSIONING',
                'fecha_primera_reaccion': '1966-04-28T00:00:00'
              }
            }

    """
    success = None
    data = UsuarioModel()
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with UsuarioService(cursor=cursor) as reactor_service:
            data = reactor_service.inventarios_repository.get_by_id(identificador)
            if data is not None:
                data = reactor_service.inventarios_repository.update(
                    identificador, reactor
                )
                message = "Se obtuvo el resultado exitosamente."
                success = True
            else:
                message = f"Reactor {identificador} no encontrado"
                status_code = 404
                data = UsuarioModel()
                success = False
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = UsuarioModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        respuesta = UsuarioCollection(success=success, msg=message, data=data)

    return respuesta
