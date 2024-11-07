"""Modulo con las clases correspondientes al repository de la tabla REACTORES en
    la base de datos."""

# External libraries
from abc import ABC

from bson import ObjectId
from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from pymongo import ReturnDocument
from sqlmodel import Session

from models.productos_model import ProductoModel


class ProductoRepository(ABC):
    """Repositorio correspondiente a las Ubicaciones de los productos."""

    def __init__(self, session: Session) -> None:
        """Crea una nueva instancia del repositorio y la conexion de Mongo.

        Args:
            session: MongoDb session.
        """
        self._session = session

    def get_by_id(self, identificador: str) -> dict:
        """Obtiene la informacion de un producto segun su identificador

        Args:
            identificador (str): Identificador ObjectId de MongoDb

        Returns:
            Informacion correspondiente al producto

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_producto': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        respuesta = self._session.productos.find_one({"_id": ObjectId(identificador)})
        return respuesta

    def get_list(self) -> list:
        """Obtener todos los productos registrados en la colleccion de Mongo Db

        Returns:
            Todos los productos

            .. code-block:: python

                [
                    {
                      'id': '662d0d325363bbc93a0c027c',
                      'nombre_producto': 'SUR Hannover',
                      'pais': 'Germany',
                      'ciudad': 'Hannover',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0.001,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1971-12-09T00:00:00'
                    },
                    {
                      'id': '662d0d325363bbc93a0c027f',
                      'nombre_producto': 'SUR Munich',
                      'pais': 'Germany',
                      'ciudad': 'Munich',
                      'tipo': 'HOMOG (S)',
                      'potencia_termica': 0,
                      'estado': 'DECOMMISSIONED',
                      'fecha_primera_reaccion': '1962-02-01T00:00:00'
                    }
                ]

        """
        productos = self._session.productos.find({})
        respuesta = list(productos)
        return respuesta

    def add(self, record: ProductoModel) -> dict:
        """Crea un nuevo registro en la coreccion de productos

        Args:
            record (ProductoModel): informacion del producto a agregar a la colleccion

        Returns:
            Informacion del producto agregado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_producto': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """

        imagekit = ImageKit(
            private_key="private_rx/LSSWw6iX7a/35hmJExP4MTV0=",
            public_key="public_pTzd+3tTVcO0ESBlro7/iSCGy1k=",
            url_endpoint="https://ik.imagekit.io/muk5lqji5",
        )

        upload = imagekit.upload_file(
            file=record.imagen,
            file_name=f"{record.imagen[0:10]}.png",
        )

        print("raw", upload.response_metadata.raw)
        imagen_url = upload.response_metadata.raw.get("url")
        record.imagen = imagen_url

        nuevo_producto = self._session.productos.insert_one(
            record.model_dump(by_alias=True, exclude=["id"])
        )
        producto_creado = self._session.productos.find_one(
            {"_id": nuevo_producto.inserted_id}
        )

        return producto_creado

    def update(self, identificador: str, record: ProductoModel) -> dict:
        """Actualiza informacion de un producto segun su identificador.

        Args:
            identificador (str): Identificador del producto a actualizar informacion.
            record (ProductoModel): Informacion que se actualizara del registro.

        Returns:
            Informacion del producto actualizado

            .. code-block:: python

                {
                    'id': '662d0d325363bbc93a0c027c',
                    'nombre_producto': 'SUR Hannover',
                    'pais': 'Germany',
                    'ciudad': 'Hannover',
                    'tipo': 'HOMOG (S)',
                    'potencia_termica': 0.001,
                    'estado': 'DECOMMISSIONED',
                    'fecha_primera_reaccion': '1971-12-09T00:00:00'
                }

        """
        producto = {
            clave: valor
            for clave, valor in record.model_dump(by_alias=True).items()
            if valor is not None
        }

        if len(producto) >= 1:
            producto_actualizado = self._session.productos.find_one_and_update(
                {"_id": ObjectId(identificador)},
                {"$set": producto},
                return_document=ReturnDocument.AFTER,
            )

        return producto_actualizado

    def delete(self, identificador: str):
        """Elimina un producto segun su identificador en la coleccion de productos.

        Args:
            identificador (str): Identificador del producto a actualizar informacion.

        Returns:
            Elementos eliminados de la colleccion.

        """
        record = self._session.productos.delete_one({"_id": ObjectId(identificador)})

        return record
