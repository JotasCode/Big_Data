import csv
import os
from datetime import date, datetime
#from tabulate import tabulate

ARCHIVO_CSV = "registro_personas.csv"
CAMPOS = [
    "id", "cedula", "nombre", "apellido", "sexo", "fecha_nacimiento", "edad", "ocupacion", "empresa", "tipo_contrato", "es_asegurado", "tipo_sangre", "direccion", "telefono_residencial", "telefono_celular"
]

#------------- Funciones Auxiliares ---------------------
def calcular_edad():
    pass

def inicializar_csv():
    pass

def obtener_datos():
    pass

def obtener_siquiente_id():
    pass

#------------- Funciones CRUD ---------------------
def crear_registros():
    print("Se ha ejecutado la función 'Crear Nuevo Registro'")

def leer_registros():
    print("Se ha ejecutado la función 'Mostrar Todos los Registros'")

def actualizar_registros():
    print("Se ha ejecutado la función 'Actualizar Registro por ID'")

def eleminar_registros():
    print("Se ha ejecutado la función 'Eliminar Registro por ID'")

def menu_principal():
    #Inciando la función que crea el archivo csv, donde se guardarán los datos.
    inicializar_csv()
    
    #Muestra en pantalla un mensaje de bienvenida al programa.
    print("Bienvenido/a al programa de registro de personas.")
    while True:
        print("1. Crear Nuevo Registro")
        print("2. Mostrar Todos los Registros")
        print("3. Actualizar Registro por ID")
        print("4. Eliminar Registro por ID")
        print("5. Salir")

        opcion = input("Favor de digitar una de las opciones: ")

        if (opcion == "1"):
            crear_registros()
        elif (opcion == "2"):
            leer_registros()
        elif (opcion == "3"):
            actualizar_registros()
        elif (opcion == "4"):
            eleminar_registros()
        elif (opcion == "5"):
            print("Muchas gracias por utilizar nuestros servicios.")
            print("JotasCode @2025 (all rights reserved).")
        else:
            print("Opcición no valida, favor de registrar una de las opciones indicadas.")
        break


if __name__ == "__main__":
    menu_principal()