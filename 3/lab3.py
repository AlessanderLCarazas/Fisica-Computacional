def calcular_fuerza_masa_aceleracion():
    print("Elige la variable que deseas calcular:")
    print("1. Fuerza")
    print("2. Masa")
    print("3. Aceleración")
    
    opcion = int(input("Ingresa el número correspondiente (1, 2, 3): "))

    if opcion == 1:  # Calcular fuerza
        masa = float(input("Ingresa la masa (kg): "))
        if masa == 0:
            print("Error: La masa no puede ser cero.")
            return
        aceleracion = float(input("Ingresa la aceleración (m/s^2): "))
        fuerza = masa * aceleracion
        print(f"La fuerza resultante es:" ,fuerza, "N")

    elif opcion == 2:  # Calcular masa
        fuerza = float(input("Ingresa la fuerza (N): "))
        aceleracion = float(input("Ingresa la aceleración (m/s^2): "))
        if aceleracion == 0:
            print("Error: No se puede calcular la masa con aceleración cero.")
            return
        masa = fuerza / aceleracion
        print(f"La masa calculada es:" ,masa, "kg")

    elif opcion == 3:  # Calcular aceleración
        fuerza = float(input("Ingresa la fuerza (N): "))
        masa = float(input("Ingresa la masa (kg): "))
        if masa == 0:
            print("Error: La masa no puede ser cero.")
            return
        aceleracion = fuerza / masa
        print(f"La aceleración calculada es:", aceleracion, "m/s^2")
    else:
        print("Opción no válida. Intenta de nuevo.")

calcular_fuerza_masa_aceleracion()
