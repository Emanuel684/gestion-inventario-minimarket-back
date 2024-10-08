"""Modulo con el endpoint para crear un usuario y la informacion asociado a este"""

# External libraries
import traceback

from fastapi import APIRouter, Response, status

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.usuarios_model import UsuarioCollection, UsuarioModel
from services.usuario_service import UsuarioService

crear_cuenta_controller = APIRouter(prefix="/usuarios", tags=["usuarios"])


@crear_cuenta_controller.post(
    "/crear-cuenta",
    status_code=status.HTTP_201_CREATED,
    response_model=UsuarioCollection,
)
def crear_cuenta(response: Response, usuario: UsuarioModel):
    """Crea un usuario dada la informacion correspondiente al mismo.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        usuario: Informacion del usuario a crear en la base de datos

    Returns:
        Si el usuario fue creado exitosamente o no.

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                '_id': '662d10f8dd91ebe8c34a81f2',
                'nombre_reactor': 'usuario',
                'pais': 'Democratic Republic of the Congo',
                'ciudad': 'Kinshasa',
                'tipo': 'TRIGA MARK II',
                'potencia_termica': 15000,
                'estado': 'EXTENDED SHUTDOWN',
                'fecha_primera_reaccion': '1972-03-24T00:00:00'
              }
            }

    """
    success = None
    data = None
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        data = {}
        with UsuarioService(cursor=cursor) as reactor_service:
            data = reactor_service.usuarios_repository.add(usuario)

        message = "Se obtuvo el resultado exitosamente."
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = None
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        print("data: ", data)
        respuesta = UsuarioCollection(success=success, msg=message, data=data)

    return respuesta
