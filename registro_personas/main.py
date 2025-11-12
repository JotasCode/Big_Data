import csv
import os
from datetime import date, datetime
from tabulate import tabulate

ARCHIVO_CSV = "registro_personas.csv"
CAMPOS = [
    "id", "cedula", "nombre", "apellido", "sexo", "fecha_nacimiento", "edad", "ocupacion", "empresa", "tipo_contrato", "es_asegurado", "tipo_sangre", "direccion", "telefono_residencial", "telefono_celular"
]

#------------------- Funciones Auxiliares ---------------------
def calcular_edad(fecha_nacimiento_str):
    """Calcular la edad de una persona a partir de su fecha de nacimiento (YYYY-MM-DD)"""
    try:
        #Convierte la cadena de objeto date
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
    except ValueError:
        return None 
        #Retorna None si el formato es incorrecto

    hoy = date.today()

    #Resta los años
    edad = hoy.year - fecha_nacimiento.year 

    #Ajustar el mes y el día por si todavía no ha cumplido años
    if(hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento_str.day):
        edad -= 1 

    return edad 

def inicializar_csv():
    """Crear el archivo CSV con los encabezados si no existen"""
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo: 
            writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
            writer.writeheader()
            print(f"Archivo '{ARCHIVO_CSV}' creado con éxito.")

def obtener_datos():
    """Lee todos los datos del CSV y los retorna como una lista de diccionarios."""
    datos = []

    try:
        with open(ARCHIVO_CSV, "r", newline= "", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                datos.append(fila)

    except FileNotFoundError:
        pass #Si no existe, retorna lista vacía. La función crear se encarga de crearlo. 

    return datos

def obtener_siquiente_id(datos):
    """Calcula el próximo ID a partir de los datos existentes."""
    if not datos:
        return 1

    max_id = max(int(persona["id"]) for persona in datos if persona["id"].isdigit())

    return max_id + 1

#------------------- Funciones CRUD ---------------------
def crear_registros():
    """Solicita los datos y crea un nuevo registro en el CSV."""
    inicializar_csv()

    datos = obtener_datos()
    nuevo_id = obtener_siquiente_id(datos)

    print("--------- Insercion de nuevo registro de persona ---------")
    registro = {
        "id" : str(nuevo_id)
    }
    
    registro["cedula"] = input("Digite su cédula: ")
    registro["nombre"] = input("Digite su nombre: ")
    registro["apellido"] = input("Digite su apellido: ")
    registro["sexo"] = input("Digite su sexo: ")
    
    while True:
        fecha_nac_str = input("Fecha de Nacimiento (YYYY-MM-DD): ")
        edad_calculada = calcular_edad(fecha_nac_str)
        if edad_calculada is not None:
            registro["fecha_nacimiento"] = fecha_nac_str
            registro["edad"] = str(edad_calculada)
            print(f"Edad calculada: {edad_calculada} años.")
            break
        else:
            print("Formato de fecha incorrecto. Use el formato correcto (YYYY-MM-DD).")
    
    registro["ocupacion"] = input("Digite su ocupación: ")
    registro["empresa"] = input("Digite su empresa: ")
    registro["tipo_contrato"] = input("Digite su tipo de contrato: ")
    registro["es_asegurado"] = input("Digite si es asegurado/a o no (sí/no): ")
    registro["tipo_sangre"] = input("Digite su tipo de sangre: ")
    registro["direccion"] = input("Digite su dirección: ")
    registro["telefono_residencial"] = input("Digite su teléfono residencial: ")
    registro["telefono_celular"] = input("Digite su teléfono celular: ")

    datos.append(registro)

    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(datos)

        print(f"Registro con el id {nuevo_id} creado y guardado con éxito.")

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
            print("JotasCode © 2025 (all rights reserved).")
            break
        else:
            print("Opcición no valida, favor de registrar una de las opciones indicadas.")

if __name__ == "__main__":
    menu_principal()