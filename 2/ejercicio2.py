import numpy as np
import matplotlib.pyplot as plt

# Ingreso de datos por el usuario
m = float(input("Ingresa la masa del móvil (kg): "))
vi = float(input("Ingresa la velocidad inicial (m/s): "))
vf = float(input("Ingresa la velocidad final (m/s): "))
t = float(input("Ingresa el tiempo transcurrido (s): "))
d = float(input("Ingresa la distancia recorrida (m): "))

# Cálculo de la aceleración
a = (vf - vi) / t

# Cálculo de la fuerza
fuerza = m * a
print(f"La fuerza aplicada es: {fuerza} N")

# Gráfico del cambio de velocidad con el tiempo
tiempo = np.linspace(0, t, 100)
velocidad = vi + a * tiempo

plt.plot(tiempo, velocidad)
plt.title("Cambio de Velocidad con el Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)
plt.show()

