import psycopg2
from PIL import Image, ImageDraw, ImageFont

def conseguir_clientes_tenido_pelo():
    conn = psycopg2.connect(
        dbname="citas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT CL.nombreCliente, CL.apellidoCliente, C.comunaCliente, C.idsede, C.monto
        FROM Cita C
        INNER JOIN Cliente CL ON C.idCliente = CL.idCliente
        INNER JOIN Sede S ON C.idSede = S.idSede
        WHERE C.nombreServicio ILIKE '%teñido%';
    """)
    clientes = cur.fetchall()

    cur.close()
    conn.close()

    return clientes

def guardar_como_imagen(texto, nombre_archivo):
    img = Image.new('RGB', (800, 600), color = (255, 255, 255))  # Crear una imagen blanca
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    y = 50
    for line in texto.splitlines():
        d.text((50, y), line, fill=(0, 0, 0), font=font)
        y += 20
    
    img.save(nombre_archivo)

def mostrar_clientes(clientes):
    if not clientes:
        texto = "No se encontraron clientes que cumplan con los criterios."
    else:
        texto = "Clientes que se tiñen el pelo:\n\n"
        texto += "{:<20} {:<20} {:<20} {:<10} {:<10}\n".format("Nombre", "Apellido", "Comuna", "Sede", "Monto")
        for cliente in clientes:
            nombre = cliente[0]
            apellido = cliente[1]
            comuna = cliente[2]
            sede = cliente[3]
            monto = cliente[4]
            texto += "{:<20} {:<20} {:<20} {:<10} ${:<10.2f}\n".format(nombre, apellido, comuna, sede, monto)

    guardar_como_imagen(texto, 'clientes_tenido_pelo.png')

if __name__ == "__main__":
    clientes = conseguir_clientes_tenido_pelo()
    mostrar_clientes(clientes)
