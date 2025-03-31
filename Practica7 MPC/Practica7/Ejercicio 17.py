# Definir los valores de la tabla
f_x = {
    0.2: 0.9798652,
    0.4: 0.9177710,
    0.6: 0.8080348,
    0.8: 0.6386093,
    1.0: 0.3843735
}

# Definir h
h = 0.2

# Aplicar la fórmula de cinco puntos para f'(0.4)
f_prime_04 = (-25*f_x[0.2] + 48*f_x[0.4] - 36*f_x[0.6] + 16*f_x[0.8] - 3*f_x[1.0]) / (12*h)

# Aplicar la fórmula de cinco puntos para f'(0.8)
f_prime_08 = (-25*f_x[0.4] + 48*f_x[0.6] - 36*f_x[0.8] + 16*f_x[1.0]) / (12*h)

# Mostrar resultados
print(f"f'(0.4) ≈ {f_prime_04}")
print(f"f'(0.8) ≈ {f_prime_08}")