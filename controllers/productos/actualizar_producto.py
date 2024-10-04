"""Modulo con el endpoint para actualiza un producto y la informacion asociado a este
    segun su identificador."""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.productos_model import (
    UpdateproductoModel,
    productoCollection,
    productoModel,
)
from services.producto_service import ProductoService

actualizar_producto_controller = APIRouter(prefix="/productos", tags=["productos"])


@actualizar_producto_controller.put(
    "/actualizar-producto/{identificador}",
    status_code=200,
    response_model=productoCollection,
    response_model_by_alias=False,
)
def actualizar_producto(
    response: Response, identificador: str, producto: UpdateproductoModel
):
    """Actualiza la informacion correspondiente a un producto en la base de datos.

    Returns:
        Si la informacion del producto fue actualizada correctamente o no.

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                'id': '6632967e003a94e8c87d5658',
                'nombre_producto': 'Isis PRUEBA ACTUALIZACION',
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
    data = productoModel()
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with ProductoService(cursor=cursor) as producto_service:
            data = producto_service.productoes_repository.get_by_id(identificador)
            if data is not None:
                data = producto_service.productoes_repository.update(
                    identificador, producto
                )
                message = "Se obtuvo el resultado exitosamente."
                success = True
            else:
                message = f"producto {identificador} no encontrado"
                status_code = 404
                data = productoModel()
                success = False
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = productoModel()
        message = "Error al obtener el resultado"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        respuesta = productoCollection(success=success, msg=message, data=data)

    return respuesta
