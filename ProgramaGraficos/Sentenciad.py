import psycopg2
from PIL import Image, ImageDraw, ImageFont

def conseguir_clientes_corte_barba():
    conn = psycopg2.connect(
        dbname="citas",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT CL.nombreCliente, CL.apellidoCliente
        FROM Cita C
        INNER JOIN Cliente CL ON C.idCliente = CL.idCliente
        WHERE C.sexo = true AND C.nombreServicio ILIKE '%corte de pelo%' AND C.nombreServicio ILIKE '%barba%';
    """)
    clientes = cur.fetchall()

    cur.close()
    conn.close()

    return clientes

def guardar_como_imagen(texto, nombre_archivo):
    img = Image.new('RGB', (800, 600), color=(255, 255, 255)) 
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
        texto = "Clientes que se cortan el pelo y la barba:\n\n"
        for cliente in clientes:
            texto += f"{cliente[0]} {cliente[1]}\n"

    guardar_como_imagen(texto, 'clientes_peloybarba.png')

if __name__ == "__main__":
    clientes = conseguir_clientes_corte_barba()
    mostrar_clientes(clientes)
