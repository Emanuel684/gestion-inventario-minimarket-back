"""Modulo con el endpoint para eliminar un tienda por identificador (ID)"""

# External libraries
import traceback

from fastapi import APIRouter, HTTPException, Response, status

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from services.tienda_service import TiendaService

eliminar_tienda_controller = APIRouter(prefix="/tiendas", tags=["tiendas"])


@eliminar_tienda_controller.delete("/eliminar-tienda/{identificador}", status_code=200)
def elimina_tienda(response: Response, identificador: str):
    """Elimina un registro correspondiente a un tienda en la base de datos

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al tienda que queremos eliminar

    Returns:
        Si la informacion del tienda fue eliminado correctamente o no.
        Si fue eliminada correctamente regresara un status code de 204.

    """
    success = None
    data = None
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        data = "Reactor no eliminado correctamente"
        with TiendaService(cursor=cursor) as tienda_service:
            delete_result = tienda_service.tiendas_repository.delete(identificador)

        if delete_result.deleted_count != 1:
            raise HTTPException(status_code=404, detail=f"Student {id} not found")
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = None
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        if delete_result.deleted_count == 1:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        response.status_code = status_code
        res = {"success": success, "msg": message, "data": data}

    return res
