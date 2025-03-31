import numpy as np

# Datos de la tabla
t_vals = np.array([1.00, 1.01, 1.02, 1.03, 1.04])
i_vals = np.array([3.12, 3.14, 3.18, 3.24, 3.24])

L = 0.98  # Inductancia
R = 0.142  # Resistencia

# Aproximación de la derivada di/dt usando diferencias centradas
di_dt = np.zeros(len(t_vals))

for i in range(1, len(t_vals) - 1):
    di_dt[i] = (i_vals[i+1] - i_vals[i-1]) / (t_vals[i+1] - t_vals[i-1])

# Aproximaciones con diferencias hacia adelante y atrás en los extremos
di_dt[0] = (i_vals[1] - i_vals[0]) / (t_vals[1] - t_vals[0])
di_dt[-1] = (i_vals[-1] - i_vals[-2]) / (t_vals[-1] - t_vals[-2])

# Cálculo del voltaje e(t) = L * di/dt + R * i
e_vals = L * di_dt + R * i_vals

print("Valores aproximados de e(t):")
for t, e in zip(t_vals, e_vals):
    print(f"t = {t} s, e ≈ {e} V")