import random
from clases import *
from funciones import *
import psycopg2

def generar_archivo_sql(tabla: Tabla):
    nombre_tabla = tabla.conseguir_nombre_tabla()
    nombres_atributos = ', '.join(tabla.conseguir_nombres_atributos())

    sentencia = f"INSERT INTO {nombre_tabla} ({nombres_atributos}) VALUES\n"

    objetos_datos = tabla.conseguir_datos()

    for dato in objetos_datos:
        sentencia += f"""   ({', '.join(
            f"'{valor}'" if isinstance(valor, str) else str(valor) 
            for valor in dato.conseguir_valores())}),\n"""

    sentencia = sentencia[:-2] + "\n;"

    return sentencia

def insertar_en_base_datos(sentencia_sql: str):
    try:
        conexion = psycopg2.connect(
            dbname="boletas", user="postgres", password="admin", host="localhost", port="5432"
        )
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")

def main():
    """
    i_paises = Tabla('Pais', ['nombrePais'])
    i_paises.agregar_dato(Dato(['Chile']))
    
    i_regiones = Tabla('Region', ['idPais', 'nombreRegion'])
    for _ in range(len(regiones)): i_regiones.agregar_dato(Dato([1, generar_region_chilena_aleatoria()]))
    """
    i_comunas = Tabla('Comuna', ['nombreComuna'])
    for _ in range(len(comunas)): i_comunas.agregar_dato(Dato([generar_comuna_chilena_aleatoria()]))
    
    i_sedes = Tabla('Sede', ['direccion'])
    for _ in range(50): i_sedes.agregar_dato(Dato([generar_direccion_aleatoria()]))
    """
    i_servicios = Tabla('Servicio', ['nombreServicio'])
    for _ in range(10): i_servicios.agregar_dato(Dato([generar_servicio_aleatorio()]))
    
    i_utensilios = Tabla('Utensilio', ['nombreUtensilio'])
    for _ in range(10): i_utensilios.agregar_dato(Dato([generar_utensilio_aleatorio()]))
    
    i_roles = Tabla('Rol', ['nombreRol'])
    for _ in range(5): i_roles.agregar_dato(Dato([generar_rol_aleatorio()]))
    
    i_productos = Tabla('Producto', ['nombreProducto'])
    for _ in range(10): i_productos.agregar_dato(Dato([generar_producto_aleatorio()]))
    
    i_proveedores = Tabla('Proveedor', ['idComuna', 'nombreProveedor'])
    for _ in range(20): i_proveedores.agregar_dato(Dato([random.randint(1, 50), generar_proveedor_aleatorio()]))
    
    i_empleados = Tabla('Empleado', ['idSede', 'idRol', 'nombre', 'apellido'])
    for _ in range(300): i_empleados.agregar_dato(Dato([random.randint(1, 50), random.randint(1, 5), generar_nombre_aleatorio(), generar_apellido_aleatorio()]))
    
    i_sueldos = Tabla('Sueldo', ['idEmpleado', 'monto', 'fecha'])
    i_liquidaciones = Tabla('Liquidacion', ['idEmpleado', 'monto', 'fecha'])
    for id_empleado in range(1, 301):
        for año in range(2018, 2025):
            for mes in range(1, 13):
                sueldo = generar_sueldo()
                comision = generar_comision()
                i_sueldos.agregar_dato(Dato([id_empleado, sueldo, f'{año}-{mes:02d}-01']))
                i_liquidaciones.agregar_dato(Dato([id_empleado, sueldo + comision, f'{año}-{mes:02d}-25']))
    """
    i_clientes = Tabla('Cliente', ['nombre', 'apellido'])
    for _ in range(30000): i_clientes.agregar_dato(Dato([generar_nombre_aleatorio(), generar_apellido_aleatorio()]))
    """
    i_boletas = Tabla('Boleta', ['idCliente', 'idSede', 'monto', 'fecha'])
    for _ in range(100000): i_boletas.agregar_dato(Dato([random.randint(1, 30000), random.randint(1, len(i_sedes.conseguir_datos())), generar_monto(), generar_fecha_aleatoria()]))
    
    i_boleta_producto = Tabla('Boleta_Producto', ['idBoleta', 'idProducto'])
    for id_boleta in range(1, 100001):
        for id_producto in range(1, 11):
            if random.randint(1, 17) % 17 == 0:
                i_boleta_producto.agregar_dato(Dato([id_boleta, id_producto]))
    
    i_citas = Tabla('Cita', ['idSede', 'idCliente', 'fecha', 'horario'])
    for id_sede in range(1, 51):
        for id_cliente in range(1, 30001):
            if random.randint(1, 137) % 137 == 0:
                i_citas.agregar_dato(Dato([id_sede, id_cliente, generar_fecha_aleatoria(), generar_horario()]))
    
    i_sede_servicio = Tabla('Sede_Servicio', ['idSede', 'idServicio', 'valor'])
    for id_sede in range(1, 51):
        for id_servicio in range(1, random.randint(1, 11)):
            if random.randint(0, 1):
                i_sede_servicio.agregar_dato(Dato([id_sede, id_servicio, generar_precio()]))
    
    i_sede_producto = Tabla('Sede_Producto', ['idSede', 'idProducto', 'valor', 'stock'])
    for id_sede in range(1, 51):
        for id_producto in range(1, random.randint(1, 11)):
            if random.randint(0, 1):
                i_sede_producto.agregar_dato(Dato([id_sede, id_producto, generar_precio(), generar_stock()]))
    
    i_sede_utensilio = Tabla('Sede_Utensilio', ['idSede', 'idUtensilio', 'stock'])
    for id_sede in range(1, 51):
        for id_utensilio in range(1, random.randint(1, 11)):
            if random.randint(0, 1):
                i_sede_utensilio.agregar_dato(Dato([id_sede, id_utensilio, generar_stock()]))
    
    i_utensilio_proveedor = Tabla('Utensilio_Proveedor', ['idUtensilio', 'idProveedor'])
    for id_proveedor in range(1, 21):
        for id_utensilio in range(1, random.randint(1, 11)):
            if random.randint(0, 1):
                i_utensilio_proveedor.agregar_dato(Dato([id_utensilio, id_proveedor]))
    
    i_utensilio_servicio = Tabla('Utensilio_Servicio', ['idUtensilio', 'idServicio'])
    for id_servicio in range(1, 11):
        for id_utensilio in range(1, random.randint(1, 11)):
            if random.randint(0, 1):
                i_utensilio_servicio.agregar_dato(Dato([id_utensilio, id_servicio]))
    
    i_producto_proveedor = Tabla('Producto_Proveedor', ['idProducto', 'idProveedor'])
    for id_proveedor in range(1, 21):
        for id_producto in range(1, random.randint(1, 11)):
            if random.randint(0, 1):
                i_producto_proveedor.agregar_dato(Dato([id_producto, id_proveedor]))
    
    i_cita_servicio = Tabla('Cita_Servicio', ['idCita', 'idServicio'])
    for id_servicio in range(1, 11):
        for id_cita in range(1, random.randint(1, 1001)):
            if random.randint(1, 5) % 5 == 0:
                i_cita_servicio.agregar_dato(Dato([id_cita, id_servicio]))
    
    i_cita_boleta = Tabla('Cita_Boleta', ['idCita', 'idBoleta'])
    for id_boleta in range(1, len(i_boletas.conseguir_datos())):
        for _ in range(1, random.randint(1, 2   )):
            id_cita = random.randint(1, len(i_citas.conseguir_datos()))
            i_cita_boleta.agregar_dato(Dato([id_cita, id_boleta]))
    """
    tablas = [i_sedes,i_clientes,i_comunas
    
        #i_paises, i_regiones, i_comunas, i_sedes, i_servicios, i_utensilios, i_roles, i_productos,
        #i_proveedores, i_empleados, i_sueldos, i_liquidaciones, i_clientes, i_boletas,
        #i_boleta_producto, i_citas, i_sede_servicio, i_sede_producto, i_sede_utensilio,
        #i_utensilio_proveedor, i_utensilio_servicio, i_producto_proveedor, i_cita_servicio, i_cita_boleta
    ]
    
    for tabla in tablas:
        sql = generar_archivo_sql(tabla)
        insertar_en_base_datos(sql)

if __name__ == "__main__":
    main()
