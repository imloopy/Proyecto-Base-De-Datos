import random
from datetime import timedelta
from datos import *

def generar_comuna_chilena_aleatoria():
    comuna_seleccionada = random.choice(comunas)
    comunas.remove(comuna_seleccionada)  # Elimina la comuna seleccionada de la lista
    return comuna_seleccionada

def generar_region_chilena_aleatoria():
    region_seleccionada = random.choice(regiones)
    regiones.remove(region_seleccionada)
    return region_seleccionada

def generar_servicio_aleatorio():
    servicio_seleccionado = random.choice(servicios)
    servicios.remove(servicio_seleccionado)
    return servicio_seleccionado

def generar_utensilio_aleatorio():
    utensilio_seleccionado = random.choice(utensilios)
    utensilios.remove(utensilio_seleccionado)
    return utensilio_seleccionado

def generar_rol_aleatorio():
    rol_seleccionado = random.choice(roles)
    roles.remove(rol_seleccionado)
    return rol_seleccionado

def generar_producto_aleatorio():
    producto_seleccionado = random.choice(productos)
    productos.remove(producto_seleccionado)
    return producto_seleccionado

def generar_proveedor_aleatorio():
    proveedor_seleccionado = random.choice(proveedores)
    proveedores.remove(proveedor_seleccionado)
    return proveedor_seleccionado

def generar_latitud_aleatoria():
    return random.uniform(-90, 90)

def generar_longitud_aleatoria():
    return random.uniform(-180, 180)

def generar_direccion_aleatoria():
    return f"{random.choice(nombres_de_calle)} {random.choice(numeros_de_calle)}"

def generar_rut_aleatorio():
    return ruts.pop(random.randint(0, len(ruts) - 1))

def generar_costo_por_watt():
    return round(random.uniform(10, 100), 2)

def generar_fecha_aleatoria():
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

def generar_nombre_aleatorio():
    return random.choice(nombres)

def generar_apellido_aleatorio():
    return random.choice(apellidos)

def generar_horario():
    return f'{random.randint(10,21)}:00'

def generar_sueldo():
    return round(random.uniform(400000, 1500000))

def generar_comision():
    return round(random.uniform(0, 300000))

def generar_precio():
    return round(random.uniform(5000, 80000))

def generar_monto():
    return round(random.uniform(5000, 200000))

def generar_stock():
    return round(random.uniform(0, 100))

def generar_num_id(number: int) -> str:
    return f"{number:05d}"

def conseguir_id_aleatorio(datos: list, tipo:str) -> str:
    return random.choice(datos).conseguir_valor(f"id_{tipo}")

def generar_sentencias_sql(datos: list):
    sentencias = f"""INSERT INTO {datos[0].conseguir_nombre_entidad()} ({', '.join(datos[0].conseguir_nombres_atributos())}) VALUES\n"""

    for dato in datos:
        valores = dato.conseguir_valores()
        for i, valor in enumerate(valores):
            if isinstance(valor, datetime.date):
                valores[i] = valor.strftime('%d-%m-%Y')

        sentencias += f"\t({valores}),\n".replace('[','').replace(']','')

    sentencias = sentencias[:-2] + "\n;"

    return sentencias

def buscar_en(datos: list, tipo: str, valor: str):
    for dato in datos:
        if dato.conseguir_valor(tipo) == valor:
            return dato