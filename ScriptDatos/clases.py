class Tabla:
    def __init__(self,
                 nombre_tabla: str,
                 nombres_atributos: list):
        self.nombre_tabla = nombre_tabla
        self.nombres_atributos = nombres_atributos
        self.datos = []

    def agregar_dato(self, dato):
        self.datos.append(dato)

    def conseguir_datos(self):
        return self.datos

    def conseguir_nombres_atributos(self):
        return self.nombres_atributos

    def conseguir_nombre_tabla(self):
        return self.nombre_tabla
    

class Dato:
    def __init__(self, 
                 valores_atributos: list):
        self.valores_atributos = valores_atributos

    def conseguir_valores(self):
        return self.valores_atributos