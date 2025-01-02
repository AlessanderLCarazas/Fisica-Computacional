def desplazamiento_constante(v, delta_t):
    return v * delta_t

def desplazamiento_acelerado(vi, alpha, delta_t):
    return vi * delta_t + 0.5 * alpha * delta_t**2

def velocidad_final(vi, alpha, delta_t):
    return vi + alpha * delta_t

def main():
    print("Bienvenido a la calculadora de ecuaciones de movimiento.")
    print("Elija una ecuación:")
    print("1. Δx = v × Δt")
    print("2. Δx = Vi × Δt + 0.5 × α × Δt^2")
    print("3. Vf = Vi + α × Δt")
    
    ecuacion = input("Ingrese el número de la ecuación que desea resolver: ")

    if ecuacion == "1":
        print("\nUsted eligió: Δx = v × Δt")
        print("¿Qué variable desea calcular?")
        print("1. Δx (Desplazamiento)")
        print("2. v (Velocidad)")
        print("3. Δt (Tiempo)")
        variable = input("Ingrese el número de la variable que desea calcular: ")
        
        if variable == "1":
            v = float(input("Ingrese el valor de la velocidad (v): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = desplazamiento_constante(v, delta_t)
            print(f"El desplazamiento (Δx) es: {resultado} metros.")
        
        elif variable == "2":
            delta_x = float(input("Ingrese el valor del desplazamiento (Δx): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = delta_x / delta_t
            print(f"La velocidad (v) es: {resultado} m/s.")
        
        elif variable == "3":
            delta_x = float(input("Ingrese el valor del desplazamiento (Δx): "))
            v = float(input("Ingrese el valor de la velocidad (v): "))
            resultado = delta_x / v
            print(f"El tiempo (Δt) es: {resultado} segundos.")
    
    elif ecuacion == "2":
        print("\nUsted eligió: Δx = Vi × Δt + 0.5 × α × Δt^2")
        print("¿Qué variable desea calcular?")
        print("1. Δx (Desplazamiento)")
        print("2. Vi (Velocidad Inicial)")
        print("3. α (Aceleración)")
        print("4. Δt (Tiempo)")
        variable = input("Ingrese el número de la variable que desea calcular: ")
        
        if variable == "1":
            vi = float(input("Ingrese el valor de la velocidad inicial (Vi): "))
            alpha = float(input("Ingrese el valor de la aceleración (α): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = desplazamiento_acelerado(vi, alpha, delta_t)
            print(f"El desplazamiento (Δx) es: {resultado} metros.")
        
        elif variable == "2":
            delta_x = float(input("Ingrese el valor del desplazamiento (Δx): "))
            alpha = float(input("Ingrese el valor de la aceleración (α): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = (delta_x - 0.5 * alpha * delta_t**2) / delta_t
            print(f"La velocidad inicial (Vi) es: {resultado} m/s.")
        
        elif variable == "3":
            delta_x = float(input("Ingrese el valor del desplazamiento (Δx): "))
            vi = float(input("Ingrese el valor de la velocidad inicial (Vi): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = 2 * (delta_x - vi * delta_t) / (delta_t**2)
            print(f"La aceleración (α) es: {resultado} m/s².")
        
        elif variable == "4":
            vi = float(input("Ingrese el valor de la velocidad inicial (Vi): "))
            alpha = float(input("Ingrese el valor de la aceleración (α): "))
            delta_x = float(input("Ingrese el valor del desplazamiento (Δx): "))
            # Se resuelve como una ecuación cuadrática del tipo at^2 + bt + c = 0
            from math import sqrt
            a = 0.5 * alpha
            b = vi
            c = -delta_x
            discriminante = b**2 - 4 * a * c
            if discriminante < 0:
                print("No hay solución real para los valores ingresados.")
            else:
                t1 = (-b + sqrt(discriminante)) / (2 * a)
                t2 = (-b - sqrt(discriminante)) / (2 * a)
                print(f"El tiempo (Δt) tiene dos posibles soluciones: {t1} segundos o {t2} segundos.")

    elif ecuacion == "3":
        print("\nUsted eligió: Vf = Vi + α × Δt")
        print("¿Qué variable desea calcular?")
        print("1. Vf (Velocidad Final)")
        print("2. Vi (Velocidad Inicial)")
        print("3. α (Aceleración)")
        print("4. Δt (Tiempo)")
        variable = input("Ingrese el número de la variable que desea calcular: ")
        
        if variable == "1":
            vi = float(input("Ingrese el valor de la velocidad inicial (Vi): "))
            alpha = float(input("Ingrese el valor de la aceleración (α): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = velocidad_final(vi, alpha, delta_t)
            print(f"La velocidad final (Vf) es: {resultado} m/s.")
        
        elif variable == "2":
            vf = float(input("Ingrese el valor de la velocidad final (Vf): "))
            alpha = float(input("Ingrese el valor de la aceleración (α): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = vf - alpha * delta_t
            print(f"La velocidad inicial (Vi) es: {resultado} m/s.")
        
        elif variable == "3":
            vf = float(input("Ingrese el valor de la velocidad final (Vf): "))
            vi = float(input("Ingrese el valor de la velocidad inicial (Vi): "))
            delta_t = float(input("Ingrese el valor del tiempo (Δt): "))
            resultado = (vf - vi) / delta_t
            print(f"La aceleración (α) es: {resultado} m/s².")
        
        elif variable == "4":
            vf = float(input("Ingrese el valor de la velocidad final (Vf): "))
            vi = float(input("Ingrese el valor de la velocidad inicial (Vi): "))
            alpha = float(input("Ingrese el valor de la aceleración (α): "))
            resultado = (vf - vi) / alpha
            print(f"El tiempo (Δt) es: {resultado} segundos.")
    
    else:
        print("Opción no válida. Por favor, elija una ecuación válida.")

if __name__ == "__main__":
    main()
