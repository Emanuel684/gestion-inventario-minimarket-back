"""Modulo con el endpoint para eliminar un reactor por identificador (ID)"""

# External libraries
import traceback

from fastapi import APIRouter, HTTPException, Response, status

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from services.reactor_service import ReactorService

eliminar_reactor_controller = APIRouter(prefix="/tiendas", tags=["tiendas"])


@eliminar_reactor_controller.delete(
    "/eliminar-reactor/{identificador}", status_code=200
)
def elimina_reactor(response: Response, identificador: str):
    """Elimina un registro correspondiente a un reactor en la base de datos

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: ID que identifica al reactor que queremos eliminar

    Returns:
        Si la informacion del reactor fue eliminado correctamente o no.
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
        with ReactorService(cursor=cursor) as reactor_service:
            delete_result = reactor_service.reactores_repository.delete(identificador)

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
