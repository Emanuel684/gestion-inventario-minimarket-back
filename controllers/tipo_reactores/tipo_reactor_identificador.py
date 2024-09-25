"""Modulo con el endpoint para obtener tipo de reactor por identificador (ID).
    La respuesta incluye todos los reactores asociados al tipo."""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.reactores_model import ReactoresCollection
from services.tipo_reactor_service import TipoReactorService

tipo_reactor_identificador_controller = APIRouter(
    prefix="/tipo-reactores", tags=["tipo_reactores"]
)


@tipo_reactor_identificador_controller.get(
    "/tipo-reactores-identificador/{identificador}",
    status_code=200,
    response_model=ReactoresCollection,
    response_model_by_alias=False,
)
def tipo_reactores_identificador(response: Response, identificador: str):
    """Obtiene todos los tipo de reactor por identificador (ID). La respuesta
        incluye todos los reactores asociados al tipo.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        identificador: Identificador del tipo de reactor a consultar

    Returns:
        Todos los tipo de reactor por identificador (ID). La respuesta
            incluye todos los reactores asociados al tipo.

        .. code-block:: python

            {
              'data': [
                {
                  'id': '662d0d325363bbc93a0c0425',
                  'nombre_reactor': 'PBR Plum Brook Reactor',
                  'pais': 'United States of America',
                  'ciudad': 'Sandusky, OH',
                  'tipo': 'TANK',
                  'potencia_termica': 60000,
                  'estado': 'DECOMMISSIONED',
                  'fecha_primera_reaccion': '1961-01-01T00:00:00'
                },
                {
                  'id': '662d0d325363bbc93a0c0553',
                  'nombre_reactor': 'HFETR',
                  'pais': 'China',
                  'ciudad': 'Chengdu',
                  'tipo': 'TANK',
                  'potencia_termica': 125000,
                  'estado': 'OPERATIONAL',
                  'fecha_primera_reaccion': '1979-12-27T00:00:00'
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
            data = tipo_reactor_service.tipo_reactor_repository.get_by_id(identificador)
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
        res = ReactoresCollection(success=success, msg=message, data=data)

    return res
