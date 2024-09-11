"""Modulo con configuraciones necesaria en el api"""

# External libraries
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Clase de configuración de la aplicación, contiene todas las
    configuraciones de la aplicación."""

    database_connection_str: str = Field(
        'system/iaea_123@localhost:1523/IAEA', env='DATABASE_CONNECTION_STR'
    )

    class Config:
        env_prefix = 'prod'
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'
