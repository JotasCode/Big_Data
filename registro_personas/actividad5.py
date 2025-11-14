#Javier José Jiménez Soto
#Actividad #5
print("Actividad #5 - Estructuras de repetición")

while True:
    print("\n--- Menú de Opciones ---")
    print("Opción #1 - Quiero operarme la naríz.")
    print("Opción #2 - Quiero operarme los labios.")
    print("Opción #3 - Quiero operarme la cintura.")
    print("Opción #4 - Quiero operarme los senos.")
    print("Opción #5 - Quiero operarme los gluteos.")
    print("Opción #6 - Salir.")

    try:
        opcion = int(input("¿Qué te quieres operar? (Ingresa el número) "))

        if opcion == 1:
            print("Te quieres operar la naríz.")
        elif opcion == 2:
            print("Te quieres operar los labios.")
        elif opcion == 3:
            print("Te quieres operar la cintura.")
        elif opcion == 4:
            print("Te quieres operar los senos.")
        elif opcion == 5:
            print("Te quieres operar los gluteos.")
        elif opcion == 6:
            print("Gracias por usar este programa. Hasta su próxima visita.")
            break 
        else:
            print("Opción no válida. El número debe estar entre 1 y 6.")

    except ValueError:
        print("Error: por favor ingrese un NÚMERO ENTERO válido (1, 2, 3, 4, 5, o 6).")