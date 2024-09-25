-- Scripts de clase - Mayo 4 de 2024
-- Curso de Tópicos Avanzados de base de datos - UPB 202410
-- Emanuel Acevedo Muñoz - emanuel.acevedom@upb.edu.co

-- Proyecto: Reactores
-- Motor de Base de datos: MongoDB - 7.x

-- ***********************************
-- Abastecimiento de imagen en Docker
-- ***********************************
 
-- Descargar la imagen -- https://hub.docker.com/_/mongo
docker pull mongo:latest

-- Crear el contenedor
docker run --name mongodb-cervezas -e “MONGO_INITDB_ROOT_USERNAME=mongoadmin” -e MONGO_INITDB_ROOT_PASSWORD=unaClav3 -p 27017:27017 -d mongo:latest

-- ****************************************
-- Creación de base de datos y usuarios
-- ****************************************

-- Con usuario mongoadmin:

-- crear la base de datos
use iaea_reactores;

-- #########################################################
-- PENDIENTE: Crear el usuario con privilegios limitados
-- #########################################################

-- Creamos las collecciones ... Sin validación

-- Estilos
db.createCollection('reactores');
db.createCollection('tipos_reactores');
db.createCollection('ubicaciones');

-- Creamos las collecciones ... usando un json schema para validación
db.createCollection('reactores', {
   validator: {
  $jsonSchema: {
    bsonType: 'object',
    title: 'Los reactores registrados',
    required: [
      'nombre_reactor',
      'pais',
      'ciudad',
      'tipo',
      'potencia_termica',
      'estado'
    ],
    properties: {
      nombre_reactor: {
        bsonType: 'string',
        description: '"nombre_reactor" Debe ser una cadena de caracteres y no puede ser nulo'
      },
      pais: {
        bsonType: 'string',
        description: '"pais" Debe ser una cadena de caracteres y no puede ser nulo'
      },
      ciudad: {
        bsonType: 'string',
        description: '"ciudad" Debe ser una cadena de caracteres y no puede ser nulo'
      },
      tipo: {
        bsonType: 'string',
        description: '"tipo" Debe ser una cadena de caracteres y no puede ser nulo'
      },
      potencia_termica: {
        bsonType: 'number',
        minimum: 0,
        description: '"potencia_termica" Debe ser numérico mínimo 0 y no puede ser nulo'
      },
      estado: {
        bsonType: 'string',
        description: '"estado" Debe ser una cadena de caracteres y no puede ser nulo'
      },
      fecha_primera_reaccion: {
        bsonType: 'string',
        description: '"fecha_primera_reaccion" Debe ser una cadena de caracteres'
      },
    }
  }
}
} );

db.createCollection('tipos_reactores', {
   validator: {
      $jsonSchema: {
         bsonType: 'object',
         title: 'Los tipos de reactores que se encuentran registrados',
         required: ['tipo'],
         properties: {
            tipo: {
               bsonType: 'string',
               description: '"tipo" Debe ser una cadena de caracteres y no puede ser nulo'
            }
         }
      }
   }
} );

db.createCollection('ubicaciones', {
   validator: {
      $jsonSchema: {
         bsonType: 'object',
         title: 'Ubicaciones de los reactores',
         required: [ 'nombre_pais', 'nombre_ciudad'],
         properties: {
            nombre_pais: {
               bsonType: 'string',
               description: '"nombre_pais" Debe ser una cadena de caracteres y no puede ser nulo'
            },
            nombre_ciudad: {
               bsonType: 'string',
               description: '"nombre_ciudad" Debe ser una cadena de caracteres y no puede ser nulo'
            },
         }
      }
   }
} );
