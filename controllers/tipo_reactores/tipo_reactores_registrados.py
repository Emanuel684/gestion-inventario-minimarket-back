"""Modulo con el endpoint para obtener todos los tipo de reactores registrados
    en la base de datos."""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.tipos_reactores_model import TiposReactoresCollection
from services.tipo_reactor_service import TipoReactorService

tipo_reactores_registrados_controller = APIRouter(
    prefix="/tipo-reactores", tags=["tipo_reactores"]
)


@tipo_reactores_registrados_controller.get(
    "/tipo-reactores-registrados",
    status_code=200,
    response_model=TiposReactoresCollection,
    response_model_by_alias=False,
)
# @wrapper
def tipo_reactores_registrados(response: Response):
    """Obtiene todos los tipo de reactores registrados en la base de datos.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todos los tipo de reactores registrados en la base de datos.

        .. code-block:: python

            {
              'data': [
                {
                  'id': '662cf9395363bbc93a0c00d9',
                  'tipo': 'TANK'
                },
                {
                  'id': '662cf9395363bbc93a0c00d6',
                  'tipo': 'HEAVY WATER'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }


    """
    success = None
    data = None
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with TipoReactorService(cursor=cursor) as tipo_reactor_service:
            data = tipo_reactor_service.tipo_reactor_repository.get_list()
        message = "Se obtuvo el resultado exitosamente."
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = None
        message = f"Error al obtener el resultado {traceback.format_exc()}"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        res = TiposReactoresCollection(success=success, msg=message, data=data)

    return res
