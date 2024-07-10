import tkinter as tk
import subprocess

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sentencias SQL")
        self.ventana.configure(bg="#F0FFFF")
        self.ventana.geometry("450x600")

        tamano_fuente = int(min(self.ventana.winfo_width(), self.ventana.winfo_height()) / 25)

        for i in range(10): 
            letra = chr(ord('A') + i) 
            texto_boton = f"Sentencia {letra}"
            boton = tk.Button(ventana,
                              text=texto_boton,
                              bg="#87CEEB",
                              fg="white",
                              font=("Arial", tamano_fuente, "bold"),
                              command=lambda letra=letra: self.ejecutar_script(letra))
            boton.grid(row=i % 5, column=i // 5, sticky="nsew", padx=10, pady=10)
            boton.config(width=15, height=3) 

    def ejecutar_script(self, letra):
        nombre_script = f"Sentencia{letra.lower()}.py"  # Generar nombre de archivo según letra
        try:
            subprocess.run(["python3", nombre_script], check=True)
        except subprocess.CalledProcessError as e:
            tk.messagebox.showerror("Error", f"No se pudo ejecutar {nombre_script}: {e}")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    interfaz = Interfaz(ventana_principal)
    ventana_principal.mainloop()
