import psycopg2
import matplotlib.pyplot as plt

def conseguir_servicio_mas_caro_por_peluqueria():
    conn = psycopg2.connect(
        dbname="citas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT C.idsede, C.nombreServicio, MAX(C.monto) AS max_monto
        FROM Cita C
        INNER JOIN Sede S ON C.idSede = S.idSede
        GROUP BY C.idsede, C.nombreServicio
        ORDER BY max_monto DESC;
    """)
    resultados = cur.fetchall()

    cur.close()
    conn.close()

    return resultados

def graficar_servicio_mas_caro_por_peluqueria(resultados):
    if not resultados:
        print("No hay datos disponibles para graficar.")
        return
    
    sedes = [fila[0] for fila in resultados]
    servicios = [fila[1] for fila in resultados]
    montos = [fila[2] for fila in resultados]

    fig, ax = plt.subplots(figsize=(12, 8))

    for sede in set(sedes):
        indices_sede = [i for i, s in enumerate(sedes) if s == sede]
        if indices_sede:
            etiqueta = f'Sede {sede}'
            ax.bar([servicios[i] for i in indices_sede], [montos[i] for i in indices_sede], label=etiqueta, alpha=0.7)

    ax.set_xlabel('Servicio')
    ax.set_ylabel('Monto máximo')
    ax.set_title('Servicio más caro por peluquería')
    ax.legend()

    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    resultados = conseguir_servicio_mas_caro_por_peluqueria()
    graficar_servicio_mas_caro_por_peluqueria(resultados)
