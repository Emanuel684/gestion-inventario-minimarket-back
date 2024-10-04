"""Modulo con el endpoint para obtener un reactor por identificador (ID)"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.tiendas_model import ReactorModel, TiendaCollection
from services.tienda_service import TiendaService

tienda_identificador_controller = APIRouter(prefix="/tiendas", tags=["tiendas"])


@tienda_identificador_controller.get(
    "/tienda-identificador/{identificador}",
    status_code=200,
    response_model=TiendaCollection,
    response_model_by_alias=False,
)
def tienda_identificador(response: Response, identificador: str):
    """Obtener informacion de un reactor registrado en la tabla REACTORES
        segun su ID.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al reactor que queremos consultar

    Returns:
        Información corespondiente al reactor que queremos consultar.

         .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '662d0d325363bbc93a0c027c',
                'nombre_reactor': 'SUR Hannover',
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
    data = ReactorModel()
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with TiendaService(cursor=cursor) as reactor_service:
            data = reactor_service.reactores_repository.get_by_id(identificador)
            if data is None:
                data = ReactorModel()
        message = "Se obtuvo el resultado exitosamente."
        success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = ReactorModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        res = TiendaCollection(success=success, msg=message, data=data)

    return res