-- Solucion Examen No. 3 - Abril 22 de 2024
-- Curso de Tópicos Avanzados de base de datos - UPB 202410
-- Emanuel Acevedo Muñoz - emanuel.acevedom@upb.edu.co
-- ID - 000478429

-- Proyecto: IAEA - Reactores Nucleares
-- Motor de Base de datos: Oracle XE 21c

-- ***********************************
-- Abastecimiento de imagen en Docker
-- ***********************************

-- Descargar la imagen y creamos el contenedor
docker compose -f docker-compose.oracle.yml up

-- Con el usuario system

-- Importante: Tener presente en que contenedor estás ubicado - Oracle XE
ALTER SESSION SET container=xepdb1;

-- creamos un usuario con privilegios de conexión y manipulación de objetos

-- USER SQL
CREATE USER IAEA IDENTIFIED BY "iaea_123"
DEFAULT TABLESPACE "USERS"
TEMPORARY TABLESPACE "TEMP";

-- QUOTAS
ALTER USER IAEA QUOTA UNLIMITED ON "USERS";

-- ROLES
GRANT "CONNECT" TO IAEA;
GRANT "RESOURCE" TO IAEA;

-- SYSTEM PRIVILEGES
GRANT CREATE TRIGGER TO IAEA;
GRANT CREATE MATERIALIZED VIEW TO IAEA;
GRANT CREATE VIEW TO IAEA;
GRANT CREATE TABLE TO IAEA;
GRANT CREATE PROCEDURE TO IAEA;

-- ==============================================================
-- Con el usuario: IAEA
-- ==============================================================

-- *******************************
-- Creacion de tablas
-- *******************************

-- -----------------------
-- Tabla Paises
-- -----------------------
CREATE TABLE IAEA.PAISES (
	ID NUMBER GENERATED AS IDENTITY CONSTRAINT IAEA_PAISES_PK PRIMARY KEY,
	NOMBRE VARCHAR2(100) NOT NULL
);

COMMENT ON TABLE IAEA.PAISES IS 'Paises de los diferentes reactores.';
COMMENT ON COLUMN IAEA.PAISES.ID IS 'Identificador del pais.';
COMMENT ON COLUMN IAEA.PAISES.NOMBRE IS 'Nombre del pais registrado.';


-- -----------------------
-- Tabla Ciudades
-- -----------------------
CREATE TABLE IAEA.CIUDADES (
	ID NUMBER GENERATED AS IDENTITY CONSTRAINT IAEA_CIUDADES_PK PRIMARY KEY,
	PAIS_ID NUMBER NOT NULL,
	NOMBRE VARCHAR2(100) NOT NULL
);

COMMENT ON TABLE IAEA.CIUDADES
    IS 'Ciudades donde se encuentran los reactores.';
COMMENT ON COLUMN IAEA.CIUDADES.ID
    IS 'Identificador de la ciudad.';
COMMENT ON COLUMN IAEA.CIUDADES.PAIS_ID
    IS 'Identificador del pais correspondiente a la ciudad.';
COMMENT ON COLUMN IAEA.CIUDADES.NOMBRE
    IS 'Nombre de la ciudad registrada.';

ALTER TABLE IAEA.CIUDADES
ADD CONSTRAINT CIUDADES_PAISES_FK FOREIGN KEY (PAIS_ID)
REFERENCES IAEA.PAISES(ID) enable;


-- -----------------------
-- Tabla Estados Reactores
-- -----------------------
CREATE TABLE IAEA.ESTADOS_REACTORES (
	ID NUMBER GENERATED AS IDENTITY CONSTRAINT IAEA_ESTADOS_REACTORES_PK PRIMARY KEY,
	NOMBRE VARCHAR2(100) NOT NULL
);

COMMENT ON TABLE IAEA.ESTADOS_REACTORES
    IS 'Estados de funcionamiento en el cual se encuentra un reactor.';
COMMENT ON COLUMN IAEA.ESTADOS_REACTORES.ID
    IS 'Identificador del estado del reactor.';
COMMENT ON COLUMN IAEA.ESTADOS_REACTORES.NOMBRE
    IS 'Nombre del estado del reactor.';


-- -----------------------
-- Tabla Tipo reactores
-- -----------------------
CREATE TABLE IAEA.TIPO_REACTORES (
	ID NUMBER GENERATED AS IDENTITY CONSTRAINT IAEA_TIPO_REACTORES_PK PRIMARY KEY,
	NOMBRE VARCHAR2(100) NOT NULL
);

COMMENT ON TABLE IAEA.TIPO_REACTORES
    IS 'Tipos de reactores registrados.';
COMMENT ON COLUMN IAEA.TIPO_REACTORES.ID
    IS 'Identificador de los diferentes tipos de reactores.';
COMMENT ON COLUMN IAEA.TIPO_REACTORES.NOMBRE
    IS 'Nombre correspondiente al tipo de reactor.';



-- -----------------------
-- Tabla Reactores
-- -----------------------
CREATE TABLE IAEA.REACTORES (
	ID NUMBER GENERATED AS IDENTITY CONSTRAINT IAEA_REACTORES_PK PRIMARY KEY,
	TIPO_REACTOR_ID NUMBER NOT NULL,
	ESTADO_REACTOR_ID NUMBER NOT NULL,
	CIUDAD_ID NUMBER NOT NULL,
	NOMBRE VARCHAR2(50) NOT NULL,
	POTENCIA_TERMICA NUMBER NOT NULL,
	FECHA_PRIMERA_REACCION DATE NULL
);

COMMENT ON TABLE IAEA.REACTORES
    IS 'REACTORES de medición.';
COMMENT ON COLUMN IAEA.REACTORES.ID
    IS 'Identificador de la zona hidrográfica de la estación.';
COMMENT ON COLUMN IAEA.REACTORES.TIPO_REACTOR_ID
    IS 'Identificador de la estación.';
COMMENT ON COLUMN IAEA.REACTORES.ESTADO_REACTOR_ID
    IS 'Identificador del municipio.';
COMMENT ON COLUMN IAEA.REACTORES.CIUDAD_ID
    IS 'Nombre de la estación registrada.';
COMMENT ON COLUMN IAEA.REACTORES.NOMBRE
    IS 'Código de la estación.';
COMMENT ON COLUMN IAEA.REACTORES.POTENCIA_TERMICA
    IS 'Latitud donde está ubicada de la estación.';
COMMENT ON COLUMN IAEA.REACTORES.FECHA_PRIMERA_REACCION
    IS 'Longitud donde está ubicada de la estación.';

ALTER TABLE IAEA.REACTORES
ADD CONSTRAINT REACTORES_CIUDADES_FK FOREIGN KEY (CIUDAD_ID)
REFERENCES IAEA.CIUDADES (ID) enable;

ALTER TABLE IAEA.REACTORES
ADD CONSTRAINT REACTORES_ESTADOS_REACTORES_FK FOREIGN KEY (ESTADO_REACTOR_ID)
REFERENCES IAEA.ESTADOS_REACTORES(ID) enable;

ALTER TABLE IAEA.REACTORES
ADD CONSTRAINT REACTORES_TIPO_REACTORES_FK FOREIGN KEY (TIPO_REACTOR_ID)
REFERENCES IAEA.TIPO_REACTORES(ID) enable;


-- -----------------------
-- Procedimiento: P_INSERTA_REACTOR
-- -----------------------
CREATE OR REPLACE PROCEDURE IAEA.P_INSERTA_REACTOR (
    P_TIPO_REACTOR_ID IN NUMBER,
    P_ESTADO_REACTOR_ID IN NUMBER,
    P_CIUDAD_ID IN NUMBER,
    P_NOMBRE IN VARCHAR2,
    P_POTENCIA_TERMICA IN NUMBER,
    P_FECHA_PRIMERA_REACCION IN VARCHAR2
) AS
    L_TOTAL_REGISTROS NUMBER;
BEGIN
    -- Verificar si ya existe un registro para la combinación dada
    SELECT COUNT(*)
    INTO L_TOTAL_REGISTROS
    FROM IAEA.REACTORES
    WHERE TIPO_REACTOR_ID = P_TIPO_REACTOR_ID
    AND ESTADO_REACTOR_ID = P_ESTADO_REACTOR_ID
    AND CIUDAD_ID = P_CIUDAD_ID
    AND NOMBRE = P_NOMBRE;

    -- Si no hay registros, insertar uno nuevo
    IF L_TOTAL_REGISTROS = 0 THEN
        INSERT INTO IAEA.REACTORES (
            TIPO_REACTOR_ID,
            ESTADO_REACTOR_ID,
            CIUDAD_ID,
            NOMBRE,
            POTENCIA_TERMICA,
            FECHA_PRIMERA_REACCION
        ) VALUES (
            P_TIPO_REACTOR_ID,
            P_ESTADO_REACTOR_ID,
            P_CIUDAD_ID,
            P_NOMBRE,
            P_POTENCIA_TERMICA,
            TO_DATE(P_FECHA_PRIMERA_REACCION, 'YYYY-MM-DD')
        );
    END IF;
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        -- Manejo de errores
        NULL; -- Opción: Registro de errores en una tabla de registro de errores
END P_INSERTA_REACTOR;


-- -----------------------
-- Para llamar el procedimiento
-- P_INSERTA_REACTOR:
-- L_TIPO_REACTOR_ID
-- L_ESTADO_REACTOR_ID
-- L_CIUDAD_ID
-- L_NOMBRE
-- L_POTENCIA_TERMICA
-- L_FECHA_PRIMERA_REACCION
-- -----------------------
DECLARE
  L_TIPO_REACTOR_ID NUMBER := 1;
  L_ESTADO_REACTOR_ID NUMBER := 1;
  L_CIUDAD_ID NUMBER := 1;
  L_NOMBRE VARCHAR2(200) := 'REACTOR';
  L_POTENCIA_TERMICA NUMBER := 15000;
  L_FECHA_PRIMERA_REACCION VARCHAR2(200) := '2020-03-31';
BEGIN
  IAEA.P_INSERTA_REACTOR(
    L_TIPO_REACTOR_ID,        -- P_TIPO_REACTOR_ID
    L_ESTADO_REACTOR_ID,      -- P_ESTADO_REACTOR_ID
    L_CIUDAD_ID,              -- P_CIUDAD_ID
    L_NOMBRE,                 -- P_NOMBRE
    L_POTENCIA_TERMICA,       -- P_POTENCIA_TERMICA
    L_FECHA_PRIMERA_REACCION  -- P_FECHA_PRIMERA_REACCION
  );
END;




-- -----------------------
-- Procedimiento: P_ACTUALIZA_REACTOR
-- -----------------------
CREATE OR REPLACE PROCEDURE IAEA.P_ACTUALIZA_REACTOR
    (P_ID IN NUMBER, P_TIPO_RECTOR_ID IN NUMBER,  P_ESTADO_REACTOR_ID IN NUMBER,
    P_CIUDAD_ID IN NUMBER, P_NOMBRE IN VARCHAR, P_POTENCIA_TERMICA IN NUMBER,
    P_FECHA_PRIMERA_REACCION IN VARCHAR)
AS
	L_TOTAL_REGISTROS NUMBER;

BEGIN
	-- Inicializar las variables necesarias
    L_TOTAL_REGISTROS := 0;

    -- Aquí validamos si hay registros de clasificaciones de mediciones para esa medición
    -- Identificar si ya existe una clasificación creada para esa combinación
    SELECT COUNT(r.ID) INTO L_TOTAL_REGISTROS
    FROM IAEA.REACTORES r
    WHERE r.ID = P_ID;

    -- Si hay registro, se actualiza el valor y fecha
    IF L_TOTAL_REGISTROS > 0 THEN
        -- Actualizamos
        UPDATE IAEA.REACTORES R SET
            R.TIPO_REACTOR_ID = P_TIPO_RECTOR_ID,
            R.ESTADO_REACTOR_ID = P_ESTADO_REACTOR_ID,
            R.CIUDAD_ID = P_CIUDAD_ID,
            R.NOMBRE = P_NOMBRE,
            R.POTENCIA_TERMICA = P_POTENCIA_TERMICA,
            R.FECHA_PRIMERA_REACCION = TO_DATE(P_FECHA_PRIMERA_REACCION, 'YYYY-MM-DD')
        WHERE R.ID = P_ID;
    END IF;

END P_ACTUALIZA_REACTOR;


-- -----------------------
-- Para llamar el procedimiento
-- P_ACTUALIZA_REACTOR:
-- P_ID
-- P_TIPO_RECTOR_ID
-- P_ESTADO_REACTOR_ID
-- P_CIUDAD_ID
-- P_NOMBRE
-- P_POTENCIA_TERMICA
-- P_FECHA_PRIMERA_REACCION
-- -----------------------
DECLARE
  L_ID NUMBER := 11;
  L_TIPO_REACTOR_ID NUMBER := 1;
  L_ESTADO_REACTOR_ID NUMBER := 1;
  L_CIUDAD_ID NUMBER := 1;
  L_NOMBRE VARCHAR2(200) := 'REACTOR';
  L_POTENCIA_TERMICA NUMBER := 15000;
  L_FECHA_PRIMERA_REACCION VARCHAR2(200) := '2020-03-31';
BEGIN
  IAEA.P_ACTUALIZA_REACTOR(
    L_ID,
   L_TIPO_REACTOR_ID,
  L_ESTADO_REACTOR_ID,
  L_CIUDAD_ID,
  L_NOMBRE,
  L_POTENCIA_TERMICA,
  L_FECHA_PRIMERA_REACCION
  );
END;


-- -----------------------
-- Procedimiento: P_ELIMINA_REACTOR
-- -----------------------
CREATE OR REPLACE PROCEDURE IAEA.P_ELIMINA_REACTOR
    (P_ID IN NUMBER)
AS
	L_TOTAL_REGISTROS NUMBER;

BEGIN
	-- Inicializar las variables necesarias
    L_TOTAL_REGISTROS := 0;

    --Aqui validamos si hay registros de clasificaciones de mediciones para esa medicion
    -- Identificar si ya existe una clasificacion creada para esa combinación
    SELECT COUNT(r.ID) INTO L_TOTAL_REGISTROS
    FROM IAEA.REACTORES r WHERE r.ID = P_ID;

    -- Si hay registro, se actualiza el valor y fecha
    IF(L_TOTAL_REGISTROS>0) THEN
    -- Eliminamos los registros
        DELETE FROM IAEA.REACTORES R WHERE R.ID = P_ID;
    -- de lo contrario, se inserta
    END IF;

END P_ELIMINA_REACTOR;

-- -----------------------
-- Para llamar el procedimiento
-- P_ELIMINA_REACTOR:
-- P_ID
-- -----------------------
DECLARE
  L_ID NUMBER := 12;
BEGIN
  IAEA.P_ELIMINA_REACTOR(
    P_ID => L_ID
  );
END;
