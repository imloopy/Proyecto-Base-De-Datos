import psycopg2
import matplotlib.pyplot as plt

def conseguir_informacion_db():

    conn = psycopg2.connect(
        dbname="citas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
SELECT C.idSede, C.comunaSede, C.horaAgendada, COUNT(*) AS total_citas
    FROM Cita C
    INNER JOIN Sede S ON C.idSede = S.idSede
    GROUP BY C.idSede, C.comunaSede, C.horaAgendada
    ORDER BY total_citas DESC;
""")
    tablas = cur.fetchall()

    cur.close()
    conn.close()

    return tablas

def graficar_horarios_citas(tablas):
    sedes = [fila[1] for fila in tablas]
    horarios = [fila[2].strftime('%H:%M') for fila in tablas]  # Convertir a cadena de hora
    total_citas = [fila[3] for fila in tablas]

    plt.figure(figsize=(12, 6))

    for sede in set(sedes):
        indices = [j for j, x in enumerate(sedes) if x == sede]
        if indices:  # Verificar si hay índices válidos antes de graficar
            plt.bar([horarios[j] for j in indices], [total_citas[j] for j in indices], label=f'Sede {sede}', alpha=0.7)
    # Crear el gráfico de barras agrupadas por sede y hora agendada
    
    plt.xlabel('Horario')
    plt.ylabel('Total de Citas')
    plt.title('Citas por Horario y Sede')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":


    tablas = conseguir_informacion_db()
    graficar_horarios_citas(tablas)
