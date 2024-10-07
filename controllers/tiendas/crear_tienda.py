"""Modulo con el endpoint para crear un tienda y la informacion asociado a este"""

# External libraries
import traceback

from fastapi import APIRouter, Response, status

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.tiendas_model import TiendaCollection, TiendaModel
from services.tienda_service import TiendaService

crear_tienda_controller = APIRouter(prefix="/tiendas", tags=["tiendas"])


@crear_tienda_controller.post(
    "/crear-tienda",
    status_code=status.HTTP_201_CREATED,
    response_model=TiendaCollection,
)
def crear_tienda(response: Response, tienda: TiendaModel):
    """Crea un tienda dada la informacion correspondiente al mismo.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        tienda: Informacion del tienda a crear en la base de datos

    Returns:
        Si el tienda fue creado exitosamente o no.

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                '_id': '662d10f8dd91ebe8c34a81f2',
                'nombre_reactor': 'tienda',
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
        with TiendaService(cursor=cursor) as reactor_service:
            data = reactor_service.tiendas_repository.add(tienda)

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
        respuesta = TiendaCollection(success=success, msg=message, data=data)

    return respuesta
