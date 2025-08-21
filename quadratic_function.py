import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la función cuadrática
a = -3   # Coeficiente cuadrático
b = -2   # Coeficiente lineal
c = 1    # Término independiente

# Definición de la función polinomial
def f(x):
    return a * x**2 + b * x + c

# Rango de valores para x
x = np.linspace(-10, 10, 400)
y = f(x)

# Crear figura
fig, ax = plt.subplots(figsize=(8, 6))

# Graficar función
ax.plot(x, y, label=f"$f(x) = {a}x^2 + {b}x + {c}$", color="blue", linewidth=2)

# Apariencia de los ejes como GeoGebra
ax.spines['left'].set_position('zero')   # Eje Y en 0
ax.spines['bottom'].set_position('zero') # Eje X en 0
ax.spines['top'].set_color('none')       # Ocultar borde superior
ax.spines['right'].set_color('none')     # Ocultar borde derecho

# Flechas en los ejes
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)  # Flecha en X
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)  # Flecha en Y

# Cuadrícula y escala
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Etiquetas de los ejes
ax.set_xlabel("x", size=12, x=1, labelpad=-20)
ax.set_ylabel("y", size=12, y=1, labelpad=-20, rotation=0)

# Leyenda
ax.legend(loc="upper right")

plt.title("Gráfica de una función cuadrática", fontsize=14)
plt.show()
