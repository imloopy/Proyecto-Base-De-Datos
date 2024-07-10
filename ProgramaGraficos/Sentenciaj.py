import psycopg2
import matplotlib.pyplot as plt

def obtener_informacion_comunas():
    conn = psycopg2.connect(
        dbname="citas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT C.comunaCliente,
               COUNT(DISTINCT C.idCliente) AS total_clientes,
               COUNT(DISTINCT S.idSede) AS total_peluquerias,
               COUNT(DISTINCT C.idCliente) AS total_clientes_comuna
        FROM Cita C
        INNER JOIN Sede S ON C.idSede = S.idSede
        INNER JOIN Comuna CO ON C.idComuna = CO.idComuna
        GROUP BY C.comunaCliente;
    """)
    resultados = cur.fetchall()

    cur.close()
    conn.close()

    return resultados

def graficar_informacion_comunas(resultados):
    if not resultados:
        print("No hay datos disponibles para graficar.")
        return
    
    comunas = [fila[0] for fila in resultados]
    total_clientes = [fila[1] for fila in resultados]
    total_peluquerias = [fila[2] for fila in resultados]
    total_clientes_comuna = [fila[3] for fila in resultados]

    fig, ax1 = plt.subplots(figsize=(12, 8))

    ax1.bar(comunas, total_peluquerias, label='Total de Peluquerías', alpha=0.7)

    ax2 = ax1.twinx()
    ax2.plot(comunas, total_clientes, marker='o', color='tab:red', label='Total de Clientes')
    ax2.plot(comunas, total_clientes_comuna, marker='x', color='tab:blue', linestyle='--', label='Clientes Residentes')

    ax1.set_xlabel('Comuna')
    ax1.set_ylabel('Total de Peluquerías', color='tab:green')
    ax2.set_ylabel('Total de Clientes', color='tab:red')
    ax1.set_title('Información por Comuna: Peluquerías y Clientes')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    resultados = obtener_informacion_comunas()
    graficar_informacion_comunas(resultados)
