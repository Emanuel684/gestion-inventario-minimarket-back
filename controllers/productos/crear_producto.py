"""Modulo con el endpoint para crear un producto y la informacion asociado a este"""

# External libraries
import traceback

from fastapi import APIRouter, Response, status

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.productos_model import ProductoCollection, ProductoModel
from services.producto_service import ProductoService

crear_producto_controller = APIRouter(prefix="/productos", tags=["productos"])


@crear_producto_controller.post(
    "/crear-producto",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductoCollection,
)
def crear_producto(response: Response, producto: ProductoModel):
    """Crea un producto dada la informacion correspondiente al mismo.

    Args:
        response: parametro de entrada para construir la respuesta en el
            decorador wrapper.
        producto: Informacion del producto a crear en la base de datos

    Returns:
        Si el producto fue creado exitosamente o no.

        .. code-block:: python

            {
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true,
              'data': {
                '_id': '662d10f8dd91ebe8c34a81f2',
                'nombre_producto': 'producto',
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
        with ProductoService(cursor=cursor) as producto_service:
            data = producto_service.productoes_repository.add(producto)

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
        respuesta = ProductoCollection(success=success, msg=message, data=data)

    return respuesta
