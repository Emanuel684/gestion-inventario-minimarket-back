"""Modulo con el endpoint para obtener un usuario por identificador (ID)"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.usuarios_model import UsuarioCollection, UsuarioModel
from services.usuario_service import UsuarioService

iniciar_sesion_controller = APIRouter(prefix="/usuarios", tags=["usuarios"])


@iniciar_sesion_controller.get(
    "/iniciar-sesion/{identificador}",
    status_code=200,
    response_model=UsuarioCollection,
    response_model_by_alias=False,
)
def iniciar_sesion(response: Response, identificador: str):
    """Obtener informacion de un usuario registrado en la tabla REACTORES
        segun su ID.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al usuario que queremos consultar

    Returns:
        Información corespondiente al usuario que queremos consultar.

         .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '662d0d325363bbc93a0c027c',
                'nombre_usuario': 'SUR Hannover',
                'pais': 'Germany',
                'ciudad': 'Hannover',
                'tipo': 'HOMOG (S)',
                'potencia_termica': 0.001,
                'estado': 'DECOMMISSIONED',
                'fecha_primera_reaccion': '1971-12-09T00:00:00'
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

        with UsuarioService(cursor=cursor) as usuario_service:
            data = usuario_service.usuarios_repository.get_by_id(identificador)
            if data is None:
                data = UsuarioModel()
        message = "Se obtuvo el resultado exitosamente."
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = UsuarioModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        res = UsuarioCollection(success=success, msg=message, data=data)

    return res
