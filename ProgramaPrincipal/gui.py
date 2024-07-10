# gui.py
import tkinter as tk
import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="peluqueria", 
        user="postgres", 
        password="admin",
        host="localhost"
    )


def run_gui(tablas):
    conn = connect_db()
    cur = conn.cursor()

    def button_click(tabla):
        for widget in right_frame.winfo_children():
            widget.destroy()
        entries = []
        for col, columna in enumerate(tabla.columns):
            label = tk.Label(right_frame, text=columna)
            label.grid(row=col, column=0, padx=5, pady=5, sticky="w")
            entry = tk.Entry(right_frame)
            entry.grid(row=col, column=1, padx=5, pady=5, sticky="e")
            entries.append(entry)
        
        submit_button = tk.Button(right_frame, text="Submit", command=lambda: submit_entries(tabla.table_name, entries))
        submit_button.grid(row=len(tabla.columns), columnspan=2, padx=5, pady=10)

    # Función para manejar la acción del botón "Submit"
    def submit_entries(table_name, entries):
        # Obtener los valores de las entradas
        values = [entry.get() for entry in entries]
        
        # Construir la consulta SQL de inserción
        columns = ", ".join(tablas[table_name].columns)
        placeholders = ", ".join(["%s"] * len(tablas[table_name].columns))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        try:
            # Ejecutar la consulta SQL
            cur.execute(query, values)
            conn.commit()
            print("Inserción exitosa en la tabla:", table_name)
        except psycopg2.Error as e:
            print("Error al insertar en la tabla:", e)

    root = tk.Tk()
    root.title("Interfaz de Botones y Cajas de Texto")
    root.geometry("900x500")

    button_scroll_frame = tk.Frame(root, width=100)  
    button_scroll_frame.pack(side="left", fill="y")

    button_canvas = tk.Canvas(button_scroll_frame, width=200) 
    button_frame = tk.Frame(button_canvas)
    scrollbar = tk.Scrollbar(button_scroll_frame, orient="vertical", command=button_canvas.yview)
    button_canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    button_canvas.pack(side="left", fill="both", expand=True)
    button_canvas.create_window((0, 0), window=button_frame, anchor="nw")

    def on_configure(event):
        button_canvas.configure(scrollregion=button_canvas.bbox("all"))
    button_canvas.bind("<Configure>", on_configure)

    for i, tabla in enumerate(tablas.values()):
        button = tk.Button(button_frame, text=tabla.table_name, command=lambda t=tabla: button_click(t), width=15, height=2) 
        button.grid(row=i, column=0, padx=5, pady=5, sticky="w")

    right_frame = tk.Frame(root, bg="lightgrey")
    right_frame.pack(side="right", fill="both", expand=True)

    root.mainloop()
