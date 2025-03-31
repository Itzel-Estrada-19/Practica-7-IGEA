import numpy as np

def f(x):
    return np.sin(x)  # Se puede cambiar por cualquier función

x0 = np.pi / 4  # Punto donde evaluaremos la derivada

print("Aproximaciones de f'(x0) usando diferentes valores de n:")

for n in range(1, 21):
    h = 10**-n
    derivada = (f(x0 + h) - f(x0)) / h
    print(f"n = {n}, f'({x0}) ≈ {derivada}")