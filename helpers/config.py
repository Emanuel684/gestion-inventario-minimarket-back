"""Módulo de configuraciones necesarias para el funcionamiento del api."""

# External libraries
import logging

from functools import lru_cache


@lru_cache()
def get_log():
    """Creación del logger de la aplicación"""
    return logging.getLogger('uvicorn.info')
