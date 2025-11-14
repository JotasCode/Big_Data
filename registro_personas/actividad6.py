#Javier José Jiménez Soto
#Actividad #6
print("Actividad #6 - Funciones")

def insertar_datos():
    print("Estas insertando un dato.")

def ver_datos():
    print("Estas viendo los datos.")

def editar_datos():
    print("Estas editando un dato.")

def borrar_datos():
    print("Estas borrando un dato.")

def cerrar_programa():
    print("Estas cerrando el programa.")

def error():
    print("Opción no valida.")

def iniciar_programa():
    print("Estas iniciando el programa.")

    print("1. Insertar datos.")
    print("2. Ver datos.")
    print("3. Editar datos.")
    print("4. Borrar datos.")
    print("5. Cerrar programa.")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        insertar_datos()
    elif opcion == "2":
        ver_datos()
    elif opcion == "3":
        editar_datos()
    elif opcion == "4":
        borrar_datos()
    elif opcion == "5":
        cerrar_programa()
    else:
        error()
    
if __name__ == "__main__":
    iniciar_programa()