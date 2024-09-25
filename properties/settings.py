"""Modulo con configuraciones necesaria en el api"""


class Settings:
    """Clase de configuración de la aplicación, contiene todas las
    configuraciones de la aplicación."""

    usuario = "usrapp"
    password = "DFpa4iYlArwRXpI0"
    cluster = "clusterreactores.u82m331.mongodb.net"
    database_connection_str = (
        f"mongodb+srv://{usuario}:{password}@{cluster}"
        f"/?retryWrites=true&w=majority&appName=ClusterReactores&authMechanism=SCRAM-SHA-1"
    )

    class Config:
        env_prefix = "prod"
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
