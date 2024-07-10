DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
SET datestyle = 'ISO, DMY';

CREATE TABLE Sede (
    idSede SERIAL PRIMARY KEY,
    direccion VARCHAR NOT NULL
);

CREATE TABLE Cliente (
    idCliente SERIAL PRIMARY key,
    nombre VARCHAR NOT NULL,
    apellido VARCHAR NOT NULL
);

CREATE TABLE Comuna (
    idComuna SERIAL PRIMARY KEY,
    nombreComuna VARCHAR NOT NULL
);

CREATE TABLE Boleta (
    idBoleta SERIAL PRIMARY KEY,
    idCliente INT REFERENCES Cliente(idCliente),
    idSede INT REFERENCES Sede(idSede),
    idComuna INT REFERENCES Comuna(idComuna),
    monto float8 NOT NULL,
    comunaCliente VARCHAR NOT NULL,
    comunaSede VARCHAR NOT NULL
);

