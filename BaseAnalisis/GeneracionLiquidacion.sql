--Base de datos de analisis de liquidacion
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
SET datestyle = 'ISO, DMY';


CREATE TABLE Rol (
    idRol SERIAL PRIMARY key,
    nombreRol VARCHAR NOT null
);

CREATE TABLE Empleado (
    idEmpleado SERIAL PRIMARY key,
    nombreEmpleado VARCHAR NOT null,
    apellidoEmpleado VARCHAR not null
);

CREATE TABLE Liquidacion (
    idLiquidacion SERIAL PRIMARY KEY,
    idEmpleado INT REFERENCES Empleado(idEmpleado),
    monto float8 NOT NULL,
    fecha DATE NOT NULL,
    nombreRol VARCHAR NOT NULL
);

