import numpy as np
import matplotlib.pyplot as plt

m = float(input("Ingrese la masa (m) en kg: "))
h_inicial = float(input("Ingrese la altura inicial (h) en metros: "))
g = 9.81

alturas = np.linspace(h_inicial, 0, 10)

energias_cinetica = []
energias_potencial = []
energias_mecanica = []

for h in alturas:
    v = np.sqrt(2 * g * (h_inicial - h))
    EK = 0.5 * m * v**2
    EP = m * g * h
    Em = EK + EP
    
    energias_cinetica.append(EK)
    energias_potencial.append(EP)
    energias_mecanica.append(Em)
    
    print(f"Altura: {h:.2f} m, Energía Cinética (EK): {EK:.2f} J, Energía Potencial (EP): {EP:.2f} J, Energía Mecánica Total (Em): {Em:.2f} J")

plt.figure(figsize=(10, 6))
plt.plot(alturas, energias_cinetica, label="Energía Cinética (EK)")
plt.plot(alturas, energias_potencial, label="Energía Potencial (EP)")
plt.plot(alturas, energias_mecanica, label="Energía Mecánica Total (Em)", linestyle='--')

plt.xlabel("Altura (m)")
plt.ylabel("Energía (J)")
plt.title("Conservación de la Energía Mecánica")
plt.legend()
plt.grid()
plt.show()
