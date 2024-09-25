"""Modulo con el endpoint para obtener ubicacion por identificador"""

# External libraries
import traceback

from fastapi import APIRouter, Response

# Own libraries
from contexts.database import crear_cursor_mongo, crear_mongo_conexion
from helpers.config import get_log
from models.ubicaciones_model import UbicacionCollection, UbicacionModel
from services.ubicacion_service import UbicacionService

ubicacion_reactor_identificador_controller = APIRouter(
    prefix="/ubicaciones", tags=["ubicaciones"]
)


@ubicacion_reactor_identificador_controller.get(
    "/ubicacion-reactor-identificador/{identificador}",
    status_code=200,
    response_model=UbicacionCollection,
    response_model_by_alias=False,
)
def ubicacion_reactor_identificador(response: Response, identificador: str):
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
                'id': '662cfec75363bbc93a0c0125',
                'nombre_pais': 'Democratic Republic of the Congo',
                'nombre_ciudad': 'Kinshasa'
              }
            }
    """
    success = None
    data = UbicacionModel()
    status_code = 200
    message = None

    try:
        conexion = crear_mongo_conexion()
        cursor = crear_cursor_mongo(conexion)

        with UbicacionService(cursor=cursor) as ubicacion_service:
            data = ubicacion_service.ubicaciones_repository.get_by_id(identificador)
        if data is None:
            message = f"Ubicacion {identificador} no encontrado"
            status_code = 404
            data = UbicacionModel()
            success = False
        else:
            message = "Se obtuvo el resultado exitosamente."
            success = True
    except Exception:
        log = get_log()
        log.error(traceback.format_exc())

        data = UbicacionModel()
        message = f"Error al obtener el resultado {traceback.format_exc()}"
        success = False
        status_code = 500
    finally:
        response.status_code = status_code
        respuesta = UbicacionCollection(success=success, msg=message, data=data)

    return respuesta
