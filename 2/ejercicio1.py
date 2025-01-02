import math

# Ingreso de datos por el usuario
G = 6.67430e-11  # Constante de gravitación universal (m^3 kg^-1 s^-2)
M_sol = float(input("Ingresa la masa del Sol (kg): "))
r = float(input("Ingresa la distancia del planeta al Sol (m): "))

# Velocidad orbital (MRU)
def velocidad_orbital(G, M_sol, r):
    v = math.sqrt(G * M_sol / r)
    return v

# Cálculo de la velocidad
v_orbital = velocidad_orbital(G, M_sol, r)
print(f"La velocidad orbital del planeta es: {v_orbital:.2f} m/s")

# Cálculo de la fuerza estática
def fuerza_centripeta(masa_planeta, v_orbital, radio_orbita):
    F = (masa_planeta * v_orbital**2) / radio_orbita
    return F

# Ingreso de la masa del planeta
masa_planeta = float(input("Ingresa la masa del planeta (kg): "))
fuerza_estatica = fuerza_centripeta(masa_planeta, v_orbital, r)
print(f"La fuerza centrípeta que mantiene al planeta en órbita es: {fuerza_estatica:.2e} N")
