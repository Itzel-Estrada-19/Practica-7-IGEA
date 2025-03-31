import numpy as np

# Datos de la tabla
tiempo = np.array([0, 3, 5, 8, 10, 13])
distancia = np.array([0, 225, 383, 623, 742, 993])

# Aproximación de la velocidad con diferencias centradas
velocidad = np.zeros(len(tiempo))

for i in range(1, len(tiempo) - 1):
    velocidad[i] = (distancia[i+1] - distancia[i-1]) / (tiempo[i+1] - tiempo[i-1])

# Aproximaciones con diferencias hacia adelante y atrás en los extremos
velocidad[0] = (distancia[1] - distancia[0]) / (tiempo[1] - tiempo[0])
velocidad[-1] = (distancia[-1] - distancia[-2]) / (tiempo[-1] - tiempo[-2])

print("Velocidades aproximadas en cada tiempo:")
for t, v in zip(tiempo, velocidad):
    print(f"t = {t} s, v ≈ {v} m/s")