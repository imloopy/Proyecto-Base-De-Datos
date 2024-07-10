--Base de datos de analisis de cita  
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
SET datestyle = 'ISO, DMY';

CREATE TABLE Cliente (
    idCliente SERIAL PRIMARY key,
    nombreCliente VARCHAR NOT NULL,
    apellidoCliente VARCHAR NOT NULL
);

CREATE TABLE Comuna (
    idComuna SERIAL PRIMARY KEY
);

CREATE TABLE Sede (
    idSede SERIAL PRIMARY KEY
);

CREATE TABLE Servicio (
    idServicio SERIAL PRIMARY KEY
);

CREATE TABLE Empleado (
    idEmpleado SERIAL PRIMARY key,
    nombreEmpleado VARCHAR NOT NULL,
    apellidoEmpleado VARCHAR NOT NULL
);

CREATE TABLE Cita (
    idCita SERIAL PRIMARY KEY,
    idCliente INT REFERENCES Cliente(idCliente),
    idSede INT REFERENCES Sede(idSede),
    idComuna INT REFERENCES Comuna(idComuna),
    idServicio INT REFERENCES Servicio(idServicio),
    idEmpleado INT REFERENCES Empleado(idEmpleado),
    sexo BOOL NOT NULL,
    nombreServicio VARCHAR NOT NULL,
    comunaCliente VARCHAR NOT NULL,
    horaAgendada TIME NOT NULL,
    duracion INT NOT NULL,
    monto DECIMAL NOT NULL,
    nombreRol VARCHAR NOT NULL,
    fecha DATE NOT NULL,
    comunaSede VARCHAR NOT NULL,
    fechaCita DATE NOT NULL
);
