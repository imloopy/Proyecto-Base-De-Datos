from clases import *

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

    print(sentencia)

def main():

    paises = Tabla('Pais', 
                   ['nombrePais'])

    comunas = Tabla('Region',
                    ['nombre_comuna'])

    comunas = Tabla('Comuna',
                    ['nombre_comuna'])

    paises.agregar_dato(Dato(['Chile']))
    comunas.agregar_dato(Dato([]))

    generar_archivo_sql(paises)

    pass


if __name__ == "__main__":
    main()