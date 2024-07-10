import psycopg2
import matplotlib.pyplot as plt

def conseguir_clientes_con_mas_duracion_por_mes():
    conn = psycopg2.connect(
        dbname="citas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT C.idsede,
               EXTRACT(MONTH FROM C.fechaCita) AS mes,
               CL.nombreCliente,
               CL.apellidoCliente,
               SUM(C.duracion) AS total_duracion
        FROM Cita C
        INNER JOIN Cliente CL ON C.idCliente = CL.idCliente
        INNER JOIN Sede S ON C.idSede = S.idSede
        GROUP BY C.idsede, mes, CL.nombreCliente, CL.apellidoCliente
        ORDER BY total_duracion DESC;
    """)
    resultados = cur.fetchall()

    cur.close()
    conn.close()

    return resultados

def graficar_clientes_con_mas_duracion_por_mes(resultados):
    if not resultados:
        print("No hay datos disponibles para graficar.")
        return
    
    sedes = [fila[0] for fila in resultados]
    meses = [int(fila[1]) for fila in resultados]
    clientes = [f"{fila[2]} {fila[3]}" for fila in resultados]
    duraciones = [fila[4] for fila in resultados]

    fig, ax = plt.subplots(figsize=(12, 8))

    for sede in set(sedes):  # Graficar por sede
        indices_sede = [i for i, s in enumerate(sedes) if s == sede]
        for mes in sorted(set(meses)):  # Graficar por mes
            indices_mes = [i for i in indices_sede if meses[i] == mes]
            if indices_mes:
                etiqueta = f'Sede {sede}, Mes {mes}'
                ax.bar([clientes[i] for i in indices_mes], [duraciones[i] for i in indices_mes], label=etiqueta, alpha=0.7)

    ax.set_xlabel('Cliente')
    ax.set_ylabel('Total de Duración (minutos)')
    ax.set_title('Clientes con mayor duración de citas por mes')
    ax.legend()

    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    resultados = conseguir_clientes_con_mas_duracion_por_mes()
    graficar_clientes_con_mas_duracion_por_mes(resultados)
