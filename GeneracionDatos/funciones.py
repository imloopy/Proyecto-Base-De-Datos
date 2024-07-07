import random
from datetime import timedelta
from datos import *

def generar_comuna_chilena_aleatoria():
    return random.choice(comunas)

def generar_latitud_aleatoria():
    return random.uniform(-90, 90)

def generar_longitud_aleatoria():
    return random.uniform(-180, 180)

def generar_tipo_energia_aleatoria():
    return random.choice(tipos_de_energia)

def generar_direccion_aleatoria():
    return f"{random.choice(nombres_de_calle)} {random.choice(numeros_de_calle)}"

def generar_rut_aleatorio():
    return ruts.pop(random.randint(0, len(ruts) - 1))

def generar_costo_por_watt():
    return round(random.uniform(10, 100), 2)

def generar_fecha_aleatoria():
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%d-%m-%Y")

def generar_nombre_aleatorio():
    return random.choice(nombres)

def generar_apellido_aleatorio():
    return random.choice(apellidos)

def generar_consumo_electrico():
    return round(random.uniform(10000, 1000000), 2)

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