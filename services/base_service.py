"""Modulo con la clase base de todos los servicios."""

# External libraries
from abc import ABC, abstractmethod


class ServiceBase(ABC):
    """Base de los servicios"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    def commit(self):
        """Commits la transaccion actual."""
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        """Rollbacks la transaccion actual."""
        raise NotImplementedError()
