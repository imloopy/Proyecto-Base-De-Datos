import psycopg2
import matplotlib.pyplot as plt

def conseguir_informacion_db():
    conn = psycopg2.connect(
        dbname="liquidaciones",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
    SELECT e.nombreEmpleado, e.apellidoEmpleado, SUM(l.monto) AS total_ganado
    FROM Liquidacion l
    INNER JOIN Empleado e ON l.idEmpleado = e.idEmpleado
    WHERE EXTRACT(YEAR FROM l.fecha) = 2023
    GROUP BY e.nombreEmpleado, e.apellidoEmpleado
    ORDER BY total_ganado DESC;
    """)
    
    tablas = cur.fetchall()

    cur.close()
    conn.close()

    return tablas

def graficar_ganancias_peluqueros(tablas):
    nombres_empleados = [fila[0] + ' ' + fila[1] for fila in tablas]
    total_ganado = [fila[2] for fila in tablas]

    plt.figure(figsize=(10, 6))
    plt.barh(nombres_empleados, total_ganado, color='skyblue')
    plt.xlabel('Monto Ganado (en unidades monetarias)')
    plt.ylabel('Peluqueros')
    plt.title('Ganancias por Peluquero durante el 2023')
    plt.gca().invert_yaxis() 
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tablas = conseguir_informacion_db()
    graficar_ganancias_peluqueros(tablas)
