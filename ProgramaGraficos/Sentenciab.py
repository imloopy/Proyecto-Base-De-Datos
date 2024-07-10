import psycopg2
import matplotlib.pyplot as plt

def conseguir_informacion_db():
    conn = psycopg2.connect(
        dbname="boletas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
    SELECT DISTINCT ON (b.idSede)
    c.nombre,
    c.apellido,
    c.idCliente,
    b.idSede,
    b.comunaCliente,
    b.comunaSede,
    SUM(b.monto) AS total_monto
FROM Boleta b
INNER JOIN Cliente c ON b.idCliente = c.idCliente
GROUP BY c.idCliente, b.idSede, b.comunaCliente, b.comunaSede, c.nombre, c.apellido
ORDER BY b.idSede, SUM(b.monto) DESC;
    """)
    
    tablas = cur.fetchall()

    cur.close()
    conn.close()

    return tablas

def graficar_clientes_gasto(tablas):
    nombres_clientes = [f"{fila[0]} {fila[1]}" for fila in tablas]
    montos_gastados = [fila[6] for fila in tablas]

    plt.figure(figsize=(10, 6))
    plt.barh(nombres_clientes, montos_gastados, color='skyblue')
    plt.xlabel('Total Gastado (en $)')
    plt.ylabel('Clientes')
    plt.title('Clientes que Gastan Más por Peluquería')
    plt.gca().invert_yaxis()  # Invertir el eje y para ordenar de mayor a menor
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tablas = conseguir_informacion_db()
    graficar_clientes_gasto(tablas)
