import psycopg2
import matplotlib.pyplot as plt

def conseguir_horarios_concurridos_por_mes_y_año():
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
               EXTRACT(YEAR FROM C.fechaCita) AS año,
               C.horaAgendada,
               COUNT(*) AS total_citas
        FROM Cita C
        INNER JOIN Sede S ON C.idSede = S.idSede
        WHERE EXTRACT(YEAR FROM C.fechaCita) IN (2019, 2020)
        GROUP BY C.idsede, mes, año, C.horaAgendada
        ORDER BY año, mes, total_citas DESC;
    """)
    resultados = cur.fetchall()

    cur.close()
    conn.close()

    return resultados

def graficar_horarios_concurridos_por_mes_y_año(resultados):
    if not resultados:
        print("No hay datos disponibles para graficar.")
        return
    
    sedes = [fila[0] for fila in resultados]
    meses = [int(fila[1]) for fila in resultados]
    años = [int(fila[2]) for fila in resultados]
    horarios = [fila[3].strftime('%H:%M') for fila in resultados]
    total_citas = [fila[4] for fila in resultados]

    fig, ax = plt.subplots(figsize=(12, 8))

    for sede in set(sedes): 
        indices_sede = [i for i, s in enumerate(sedes) if s == sede]
        for año in sorted(set(años)): 
            indices_año = [i for i in indices_sede if años[i] == año]
            for mes in sorted(set(meses)): 
                indices_mes = [i for i in indices_año if meses[i] == mes]
                if indices_mes:
                    etiqueta = f'Sede {sede}, Año {año}, Mes {mes}'
                    ax.bar([horarios[i] for i in indices_mes], [total_citas[i] for i in indices_mes], label=etiqueta, alpha=0.7)

    ax.set_xlabel('Hora del día')
    ax.set_ylabel('Total de Citas')
    ax.set_title('Horarios más concurridos por peluquería (2019-2020)')
    ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    resultados = conseguir_horarios_concurridos_por_mes_y_año()
    graficar_horarios_concurridos_por_mes_y_año(resultados)
