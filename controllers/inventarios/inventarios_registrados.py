"""Modulo con el endpoint para obtener todos los inventarioes registrados"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.inventarios_model import InventariosCollection
from services.inventario_service import InventarioService

inventarios_registrados_controller = APIRouter(
    prefix="/inventarios", tags=["inventarios"]
)


@inventarios_registrados_controller.get(
    "/inventarios-registrados",
    status_code=200,
    response_model=InventariosCollection,
    response_model_by_alias=False,
)
def inventarios_registrados(response: Response):
    """Obtener todos los inventarioes registrados en la tabla REACTORES

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.

    Returns:
        Todos los inventarios registrados en la base de datos

        .. code-block:: python

            {
              'data': [
                {
                  'id': '662d0d325363bbc93a0c027c',
                  'nombre_inventario': 'SUR Hannover',
                  'pais': 'Germany',
                  'ciudad': 'Hannover',
                  'tipo': 'HOMOG (S)',
                  'potencia_termica': 0.001,
                  'estado': 'DECOMMISSIONED',
                  'fecha_primera_reaccion': '1971-12-09T00:00:00'
                },
                {
                  'id': '662d0d325363bbc93a0c027f',
                  'nombre_inventario': 'SUR Munich',
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
        with InventarioService(cursor=cursor) as inventario_service:
            data = inventario_service.inventarios_repository.get_list()
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
        res = InventariosCollection(data=data, success=success, msg=message)

    return res
