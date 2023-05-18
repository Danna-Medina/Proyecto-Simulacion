import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from fractions import Fraction

vertices_rectangulo = np.array([[1, 1], [5, 3], [4, 5], [0, 3]])
viewport = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])

Sx = 1 / (2 * np.sqrt(5))
Sy = 1 / np.sqrt(5)

print("Sx:", round(Sx, 5))
print("Sy:", round(Sy, 5))

N = np.array([[Sx, 0, -Sx],
              [0, -Sy, -Sy],
              [0, 0, 1]])

#matriz de transformación de normalización
print("\n\nMatriz de transformación de normalización (N):")
print(N)

m = (vertices_rectangulo[1][1] - vertices_rectangulo[0][1]) / (vertices_rectangulo[1][0] - vertices_rectangulo[0][0])
beta = np.arctan(m)
cos_beta = np.cos(beta)
sin_beta = np.sin(beta)

matriz_rotacion = np.array([[cos_beta, sin_beta, 0],
                            [-sin_beta, cos_beta, 0],
                            [0, 0, 1]])

#matriz de rotación
print("\n\nMatriz de rotación:")
print(matriz_rotacion)


NR = N.dot(matriz_rotacion)

print("\n\nMatriz de transformación de normalización requerida (NR):")
print(NR)


centro_circulo = np.array([2.5, 3, 1])
radio_circulo = Fraction(1, 3)

print("\n\nCentro del círculo:", centro_circulo)
print("Radio del círculo:", radio_circulo)


fig, ax = plt.subplots()
ax.set_aspect('equal')

def actualizar(frame):
    ax.clear()
    ax.set_aspect('equal')

    t = min(frame / 100.0, 1.0)
    centro_circulo_transformado = (1 - t) * centro_circulo[:2] + t * (viewport[0] + viewport[2]) / 2

    vertices_transformados = NR.dot(np.hstack((vertices_rectangulo, np.ones((4, 1)))).T).T[:, :2]

    min_x = np.min(vertices_transformados[:, 0])
    min_y = np.min(vertices_transformados[:, 1])
    vertices_transformados -= [min_x, min_y]

    rectangulo_original = plt.Polygon(vertices_rectangulo, closed=True, fill=None)
    ax.add_patch(rectangulo_original)

    rectangulo_transformado = plt.Polygon(vertices_transformados, closed=True, fill=None, edgecolor='g')
    ax.add_patch(rectangulo_transformado)

    circulo_original = plt.Circle(centro_circulo[:2], float(radio_circulo), edgecolor='r', fill=None)
    ax.add_patch(circulo_original)

    circulo_transformado = plt.Circle(centro_circulo_transformado, float(radio_circulo), edgecolor='b', facecolor='b')
    ax.add_patch(circulo_transformado)

    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

ani = FuncAnimation(fig, actualizar, frames=100, interval=50)

plt.show()

actualizar(0)
fig.savefig('primera_imagen.png')

actualizar(99)
fig.savefig('ultima_imagen.png')
