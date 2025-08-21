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

