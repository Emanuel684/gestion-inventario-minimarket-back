"""Modulo con el endpoint para obtener todos los reactores registrados"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.tiendas_model import TiendasCollection
from services.tienda_service import TiendaService

tiendas_registradas_controller = APIRouter(prefix="/tiendas", tags=["tiendas"])


@tiendas_registradas_controller.get(
    "/tiendas-registradas",
    status_code=200,
    response_model=TiendasCollection,
    response_model_by_alias=False,
)
def tiendas_registradas(response: Response):
    """Obtener todos los reactores registrados en la tabla REACTORES

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todos los reactores registrados en la base de datos

        .. code-block:: python

            {
              'data': [
                {
                  'id': '662d0d325363bbc93a0c027c',
                  'nombre_reactor': 'SUR Hannover',
                  'pais': 'Germany',
                  'ciudad': 'Hannover',
                  'tipo': 'HOMOG (S)',
                  'potencia_termica': 0.001,
                  'estado': 'DECOMMISSIONED',
                  'fecha_primera_reaccion': '1971-12-09T00:00:00'
                },
                {
                  'id': '662d0d325363bbc93a0c027f',
                  'nombre_reactor': 'SUR Munich',
                  'pais': 'Germany',
                  'ciudad': 'Munich',
                  'tipo': 'HOMOG (S)',
                  'potencia_termica': 0,
                  'estado': 'DECOMMISSIONED',
                  'fecha_primera_reaccion': '1962-02-01T00:00:00'
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
        with TiendaService(cursor=cursor) as reactores_service:
            data = reactores_service.tiendas_repository.get_list()
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
        res = TiendasCollection(data=data, success=success, msg=message)

    return res
