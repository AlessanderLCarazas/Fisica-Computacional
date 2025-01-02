import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Definir funciones de fuerza
def fuerza_polinomica(x):
    return 2*x**2 + 3*x + 1

def fuerza_seno(x):
    return np.sin(x)

def fuerza_coseno(x):
    return np.cos(x)

def fuerza_exp(x):
    return np.exp(x)

# Selección de la función de fuerza
def seleccionar_funcion():
    print("Seleccione la función de fuerza:")
    print("1: Polinómica (2*x^2 + 3*x + 1)")
    print("2: Seno (sin(x))")
    print("3: Coseno (cos(x))")
    print("4: Exponencial (exp(x))")
    opcion = int(input("Ingrese el número de su opción: "))

    if opcion == 1:
        return fuerza_polinomica, "Fuerza Polinómica"
    elif opcion == 2:
        return fuerza_seno, "Fuerza Senoidal"
    elif opcion == 3:
        return fuerza_coseno, "Fuerza Cosenoidal"
    elif opcion == 4:
        return fuerza_exp, "Fuerza Exponencial"
    else:
        print("Opción no válida.")
        exit()

# Calcular el trabajo usando integral y sumatoria
def calcular_trabajo(fuerza, a=0, b=1, n=1000):
    # Calcular el trabajo usando la integral
    trabajo_integral, _ = quad(fuerza, a, b)
    
    # Calcular el trabajo usando la sumatoria
    x = np.linspace(a, b, n)
    dx = (b - a) / n
    trabajo_sumatoria = np.sum(fuerza(x) * dx)
    
    # Calcular la diferencia porcentual
    diferencia_porcentual = abs((trabajo_integral - trabajo_sumatoria) / trabajo_integral) * 100
    
    return trabajo_integral, trabajo_sumatoria, diferencia_porcentual

# Graficar los resultados
def graficar_resultados(fuerza, titulo, trabajo_integral, trabajo_sumatoria, diferencia_porcentual, a=0, b=1, n=1000):
    x = np.linspace(a, b, n)
    
    plt.figure(figsize=(12, 6))
    
    # Graficar la función de fuerza
    plt.plot(x, fuerza(x), label=titulo, color='b')
    plt.fill_between(x, fuerza(x), alpha=0.3, label='Área bajo la curva (Trabajo Integral)')
    
    # Agregar líneas horizontales para el trabajo calculado
    plt.axhline(y=trabajo_integral, color='g', linestyle='--', label=f'Trabajo (Integral): {trabajo_integral:.4f}')
    plt.axhline(y=trabajo_sumatoria, color='r', linestyle='--', label=f'Trabajo (Sumatoria): {trabajo_sumatoria:.4f}')
    
    # Título y etiquetas
    plt.title(f'Comparación de Trabajo usando Integral y Sumatoria\nDiferencia Porcentual: {diferencia_porcentual:.2f}%')
    plt.xlabel('x')
    plt.ylabel('Fuerza f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecución del proceso
fuerza, titulo = seleccionar_funcion()

trabajo_integral, trabajo_sumatoria, diferencia_porcentual = calcular_trabajo(fuerza)

# Mostrar resultados numéricos
print(f"Trabajo (Integral): {trabajo_integral:.4f}")
print(f"Trabajo (Sumatoria): {trabajo_sumatoria:.4f}")
print(f"Diferencia Porcentual: {diferencia_porcentual:.2f}%")

# Graficar los resultados
graficar_resultados(fuerza, titulo, trabajo_integral, trabajo_sumatoria, diferencia_porcentual)
