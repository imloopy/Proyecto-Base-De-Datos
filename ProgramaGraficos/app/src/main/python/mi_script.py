import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend (Agg) to avoid opening a window
import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    # Datos para el gráfico
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Crear el gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='sin(x)')
    plt.title('Gráfico generado desde Python')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()

    # Guardar el gráfico como imagen
    plt.savefig('plot.png')

if __name__ == "__main__":
    generate_plot()
