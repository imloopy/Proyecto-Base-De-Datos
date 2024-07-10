DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
SET datestyle = 'ISO, DMY';

CREATE TABLE Pais (
    idPais SERIAL PRIMARY KEY,
    nombrePais VARCHAR(255) NOT NULL
);

CREATE TABLE Region (
    idRegion SERIAL PRIMARY KEY,
    idPais INT REFERENCES Pais(idPais),
    nombreRegion VARCHAR(255) NOT NULL
);

CREATE TABLE Comuna (
    idComuna SERIAL PRIMARY KEY,
    idRegion INT REFERENCES Region(idRegion),
    nombreComuna VARCHAR(255) NOT NULL
);

CREATE TABLE Sede (
    idSede SERIAL PRIMARY KEY,
    idComuna INT REFERENCES Comuna(idComuna),
    direccion VARCHAR(255) NOT NULL
);

CREATE TABLE Servicio (
    idServicio SERIAL PRIMARY KEY,
    nombreServicio VARCHAR(255) NOT NULL
);

CREATE TABLE Utensilio (
    idUtensilio SERIAL PRIMARY KEY,
    nombreUtensilio VARCHAR(255) NOT NULL
);

CREATE TABLE Rol (
    idRol SERIAL PRIMARY KEY,
    nombreRol VARCHAR(255) NOT NULL
);

CREATE TABLE Producto (
    idProducto SERIAL PRIMARY KEY,
    nombreProducto VARCHAR(255) NOT NULL
);

CREATE TABLE Proveedor (
    idProveedor SERIAL PRIMARY KEY,
    idComuna INT REFERENCES Comuna(idComuna),
    nombreProveedor VARCHAR(255) NOT NULL
);

CREATE TABLE Empleado (
    idEmpleado SERIAL PRIMARY KEY,
    idSede INT REFERENCES Sede(idSede),
    idRol INT REFERENCES Rol(idRol),
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);

CREATE TABLE Sueldo (
    idSueldo SERIAL PRIMARY KEY,
    idEmpleado INT REFERENCES Empleado(idEmpleado),
    monto DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL
);

CREATE TABLE Liquidacion (
    idLiquidacion SERIAL PRIMARY KEY,
    idEmpleado INT REFERENCES Empleado(idEmpleado),
    monto DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL
);

CREATE TABLE Cliente (
    idCliente SERIAL PRIMARY KEY,
    idComuna INT REFERENCES Comuna(idComuna),
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);

CREATE TABLE Boleta (
    idBoleta SERIAL PRIMARY KEY,
    idSede INT REFERENCES Sede(idSede),
    idCliente INT REFERENCES Cliente(idCliente),
    monto DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL
);

CREATE TABLE Boleta_Producto (
    idBoleta INT REFERENCES Boleta(idBoleta),
    idProducto INT REFERENCES Producto(idProducto),
    PRIMARY KEY (idBoleta, idProducto)
);

CREATE TABLE Cita (
    idCita SERIAL PRIMARY KEY,
    idSede INT REFERENCES Sede(idSede),
    idCliente INT REFERENCES Cliente(idCliente),
    fecha DATE NOT NULL,
    horario TIME NOT NULL
);

CREATE TABLE Sede_Servicio (
    idSede INT REFERENCES Sede(idSede),
    idServicio INT REFERENCES Servicio(idServicio),
    valor DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (idSede, idServicio)
);

CREATE TABLE Sede_Producto (
    idSede INT REFERENCES Sede(idSede),
    idProducto INT REFERENCES Producto(idProducto),
    valor DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    PRIMARY KEY (idSede, idProducto)
);

CREATE TABLE Sede_Utensilio (
    idSede INT REFERENCES Sede(idSede),
    idUtensilio INT REFERENCES Utensilio(idUtensilio),
    stock INT NOT NULL,
    PRIMARY KEY (idSede, idUtensilio)
);

CREATE TABLE Utensilio_Proveedor (
    idUtensilio INT REFERENCES Utensilio(idUtensilio),
    idProveedor INT REFERENCES Proveedor(idProveedor),
    PRIMARY KEY (idUtensilio, idProveedor)
);

CREATE TABLE Utensilio_Servicio (
    idUtensilio INT REFERENCES Utensilio(idUtensilio),
    idServicio INT REFERENCES Servicio(idServicio),
    PRIMARY KEY (idUtensilio, idServicio)
);

CREATE TABLE Producto_Proveedor (
    idProducto INT REFERENCES Producto(idProducto),
    idProveedor INT REFERENCES Proveedor(idProveedor),
    PRIMARY KEY (idProducto, idProveedor)
);

CREATE TABLE Cita_Servicio (
    idCita INT REFERENCES Cita(idCita),
    idServicio INT REFERENCES Servicio(idServicio),
    PRIMARY KEY (idCita, idServicio)
);

CREATE TABLE Cita_Boleta (
    idCita INT REFERENCES Cita(idCita),
    idBoleta INT REFERENCES Boleta(idBoleta),
    PRIMARY KEY (idCita, idBoleta)
);

ALTER SEQUENCE pais_idPais_seq RESTART WITH 1;
ALTER SEQUENCE region_idRegion_seq RESTART WITH 1;
ALTER SEQUENCE comuna_idComuna_seq RESTART WITH 1;
ALTER SEQUENCE sede_idSede_seq RESTART WITH 1;
ALTER SEQUENCE rol_idRol_seq RESTART WITH 1;
ALTER SEQUENCE empleado_idEmpleado_seq RESTART WITH 1;
ALTER SEQUENCE liquidacion_idLiquidacion_seq RESTART WITH 1;
ALTER SEQUENCE sueldo_idSueldo_seq RESTART WITH 1;
ALTER SEQUENCE cliente_idCliente_seq RESTART WITH 1;
ALTER SEQUENCE cita_idCita_seq RESTART WITH 1;
ALTER SEQUENCE servicio_idServicio_seq RESTART WITH 1;
ALTER SEQUENCE utensilio_idUtensilio_seq RESTART WITH 1;
ALTER SEQUENCE producto_idProducto_seq RESTART WITH 1;
ALTER SEQUENCE proveedor_idProveedor_seq RESTART WITH 1;
ALTER SEQUENCE boleta_idBoleta_seq RESTART WITH 1;
