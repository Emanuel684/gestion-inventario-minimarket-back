"""Modulo con el endpoint para actualiza un tienda y la informacion asociado a este
    segun su identificador."""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.tiendas_model import (ReactorCollection, ReactorModel,
                                  UpdateReactorModel)
from services.tienda_service import TiendaService

actualizar_tienda_controller = APIRouter(prefix="/tiendas", tags=["tiendas"])


@actualizar_tienda_controller.put(
    "/actualizar-tienda/{identificador}",
    status_code=200,
    response_model=ReactorCollection,
    response_model_by_alias=False,
)
def actualizar_tienda(
    response: Response, identificador: str, tienda: UpdateReactorModel
):
    """Actualiza la informacion correspondiente a un tienda en la base de datos.

    Returns:
        Si la informacion del tienda fue actualizada correctamente o no.

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '6632967e003a94e8c87d5658',
                'nombre_reactor': 'Isis PRUEBA ACTUALIZACION',
                'pais': 'France',
                'ciudad': 'Gif-sur-Yvette',
                'tipo': 'POOL',
                'potencia_termica': 700,
                'estado': 'UNDER DECOMMISSIONING',
                'fecha_primera_reaccion': '1966-04-28T00:00:00'
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
            data = reactor_service.tiendas_repository.get_by_id(identificador)
            if data is not None:
                data = reactor_service.tiendas_repository.update(identificador, tienda)
                message = "Se obtuvo el resultado exitosamente."
                success = True
            else:
                message = f"tienda {identificador} no encontrado"
                status_code = 404
                data = ReactorModel()
                success = False
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = ReactorModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        respuesta = ReactorCollection(success=success, msg=message, data=data)

    return respuesta
