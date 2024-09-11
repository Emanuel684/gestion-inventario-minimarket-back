"""Módulo con wraper para construir respuesta de endpoints."""

# External libraries
import traceback

from functools import wraps

# Own libraries
from helpers.config import get_log


def wrapper(func):
    """Wraper para la construcción de respuestas de API.

    Args:
        func: Función correspondiente al endpoint para construir respuesta.

    Returns:
        Respuesta del endpoint

        .. code-block: python

            {
              'data': [
                {
                  'ID': 481,
                  'TIPO_REACTOR_ID': 23,
                  'ESTADO_REACTOR_ID': 2,
                  'CIUDAD_ID': 137,
                  'NOMBRE': 'NTR General Electric',
                  'POTENCIA_TERMICA': 100,
                  'FECHA_PRIMERA_REACCION': '1957-11-15T00:00:00'
                }],
              'msg': 'Se obtuvo el resultado exitosamente.',
              'success': true
            }

    """

    @wraps(func)
    async def wrapper(**kwargs):
        response = kwargs['response']
        success = None
        data = None
        status_code = 200
        message = None

        try:
            data = func(**kwargs)
            message = 'Se obtuvo el resultado exitosamente.'
            success = True
        except Exception:
            log = get_log()
            log.error(traceback.format_exc())

            data = None
            message = 'Error al obtener el resultado'
            success = False
            status_code = 500
        finally:
            response.status_code = status_code
            res = {'success': success, 'msg': message, 'data': data}

        return res

    return wrapper
