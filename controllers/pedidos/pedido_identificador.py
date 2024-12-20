"""Modulo con el endpoint para obtener un pedido por identificador (ID)"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.pedidos_model import PedidoCollection, PedidoModel
from services.pedido_service import PedidoService

pedido_identificador_controller = APIRouter(prefix="/pedidos", tags=["pedidos"])


@pedido_identificador_controller.get(
    "/pedido-identificador/{identificador}",
    status_code=200,
    response_model=PedidoCollection,
    response_model_by_alias=False,
)
def pedido_identificador(response: Response, identificador: str):
    """Obtener informacion de un pedido registrado en la tabla REACTORES
        segun su ID.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al pedido que queremos consultar

    Returns:
        Información corespondiente al pedido que queremos consultar.

         .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '662d0d325363bbc93a0c027c',
                'nombre_pedido': 'SUR Hannover',
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
    data = PedidoModel()
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with PedidoService(cursor=cursor) as pedido_service:
            data = pedido_service.pedidos_repository.get_by_id(identificador)
            if data is None:
                data = PedidoModel()
        message = "Se obtuvo el resultado exitosamente."
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = PedidoModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        res = PedidoCollection(success=success, msg=message, data=data)

    return res
