"""Modulo con los modelos de la base de datos"""

# External libraries
from sqlmodel import SQLModel
from utilities.utilities import to_camel


class BaseModel(SQLModel):
    """Clase de modelo SQL base."""

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
