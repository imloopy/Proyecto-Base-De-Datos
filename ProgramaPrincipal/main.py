# main.py
from table import Table  # Importa la clase Table desde el módulo table
import gui

def main():
# Definir las tablas y columnas
    tables_columns = {
        "Pais": ["idPais", "nombrePais"],
        "Region": ["idRegion", "idPais", "nombreRegion"],
        "Comuna": ["idComuna", "idRegion", "nombreComuna"],
        "Sede": ["idSede", "idComuna", "direccion"],
        "Servicio": ["idServicio", "nombreServicio"],
        "Utensilio": ["idUtensilio", "nombreUtensilio"],
        "Rol": ["idRol", "nombreRol"],
        "Producto": ["idProducto", "nombreProducto"],
        "Proveedor": ["idProveedor", "idComuna", "nombreProveedor"],
        "Empleado": ["idEmpleado", "idSede", "idRol", "nombre", "apellido"],
        "Sueldo": ["idSueldo", "idEmpleado", "monto", "fecha"],
        "Liquidacion": ["idLiquidacion", "idEmpleado", "monto", "fecha"],
        "Cliente": ["idCliente", "idComuna", "nombre", "apellido"],
        "Boleta": ["idBoleta", "idSede", "idCliente", "monto", "fecha"],
        "Boleta_Producto": ["idBoleta", "idProducto"],
        "Cita": ["idCita", "idSede", "idCliente", "fecha", "horario"],
        "Sede_Servicio": ["idSede", "idServicio", "valor"],
        "Sede_Producto": ["idSede", "idProducto", "valor", "stock"],
        "Sede_Utensilio": ["idSede", "idUtensilio", "stock"],
        "Utensilio_Proveedor": ["idUtensilio", "idProveedor"],
        "Utensilio_Servicio": ["idUtensilio", "idServicio"],
        "Producto_Proveedor": ["idProducto", "idProveedor"],
        "Cita_Servicio": ["idCita", "idServicio"],
        "Cita_Boleta": ["idCita", "idBoleta"]
    }

    # Generar instancias de las clases Table
    tables = {table_name: Table(table_name, columns) for table_name, columns in tables_columns.items()}

    gui.run_gui(tables)

if __name__ == "__main__":
    main()
