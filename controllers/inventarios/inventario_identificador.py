"""Modulo con el endpoint para obtener un inventario por identificador (ID)"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.inventarios_model import InventarioCollection, InventarioModel
from services.inventario_service import InventarioService

inventario_identificador_controller = APIRouter(
    prefix="/inventarios", tags=["inventarios"]
)


@inventario_identificador_controller.get(
    "/inventario-identificador/{identificador}",
    status_code=200,
    response_model=InventarioCollection,
    response_model_by_alias=False,
)
def inventario_identificador(response: Response, identificador: str):
    """Obtener informacion de un inventario registrado en la tabla Inventario
        segun su ID.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al inventario que queremos consultar

    Returns:
        Información corespondiente al inventario que queremos consultar.

         .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '662d0d325363bbc93a0c027c',
                'nombre_inventario': 'SUR Hannover',
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
    data = InventarioModel()
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with InventarioService(cursor=cursor) as inventario_service:
            data = inventario_service.inventarios_repository.get_by_id(identificador)
            if data is None:
                data = InventarioModel()
        message = "Se obtuvo el resultado exitosamente."
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = InventarioModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        res = InventarioCollection(success=success, msg=message, data=data)

    return res
