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
    """Calcula la edad de una persona a partir de su fecha de nacimiento (YYYY-MM-DD)"""
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
    if(hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1 

    return edad 

def inicializar_csv():
    """Crea el archivo CSV con los encabezados si no existen"""
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

def guardar_datos(datos):
    """Escribe la lista completa de diccionarios de vuelta al archivo CSV."""
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(datos)

def obtener_siguiente_id(datos):
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
    nuevo_id = obtener_siguiente_id(datos)

    print("\n--------- Insertando un nuevo registro de persona ---------")
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
    guardar_datos(datos)

    print("-" * 50)
    print(f"\nRegistro con el id {nuevo_id} creado y guardado con éxito.")


def leer_registros():
    """Lee todos los registros del CSV y los muestra en formato tabular."""
    datos = obtener_datos()

    print("\n--------- Todos los registros de personas ---------")
    if datos:
        # Muestra los datos usando tabulate para un formato limpio
        print(tabulate(datos, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nNo hay registros de personas para mostrar. Use la opción 1 para crear uno.")


def actualizar_registros():
    """Solicita un ID y permite actualizar los campos de un registro existente."""
    datos = obtener_datos()

    print("\n--------- Actualizar registro por ID ---------")
    if not datos:
        print("No hay registros para actualizar.")
        return

    id_a_actualizar = input("Digite el ID del registro que desea actualizar: ")
    
    indice_encontrado = -1
    for i, persona in enumerate(datos):
        if persona.get("id") == id_a_actualizar:
            indice_encontrado = i
            break

    if indice_encontrado != -1:
        registro = datos[indice_encontrado]
        print(f"Registro encontrado (ID: {id_a_actualizar}). Deje el campo vacío para mantener el valor actual.")

        # Función auxiliar para solicitar y actualizar un campo
        def solicitar_campo(prompt, key):
            nuevo_valor = input(f"{prompt} (Actual: {registro.get(key, 'N/A')}): ").strip()
            return nuevo_valor if nuevo_valor else registro.get(key, "")

        # Solicitud de nuevos datos
        registro["cedula"] = solicitar_campo("Nueva cédula", "cedula")
        registro["nombre"] = solicitar_campo("Nuevo nombre", "nombre")
        registro["apellido"] = solicitar_campo("Nuevo apellido", "apellido")
        registro["sexo"] = solicitar_campo("Nuevo sexo", "sexo")

        # Manejo de la fecha de nacimiento y recálculo de edad
        fecha_nac_actual = registro.get("fecha_nacimiento", "")
        while True:
            nueva_fecha_nac_str = input(f"Nueva Fecha de Nacimiento (YYYY-MM-DD) (Actual: {fecha_nac_actual}): ").strip()
            
            if not nueva_fecha_nac_str:
                # Mantener la fecha y edad actual si no se modifica
                registro["fecha_nacimiento"] = fecha_nac_actual
                break
            
            edad_calculada = calcular_edad(nueva_fecha_nac_str)
            if edad_calculada is not None:
                registro["fecha_nacimiento"] = nueva_fecha_nac_str
                registro["edad"] = str(edad_calculada)
                print(f"Edad recalculada: {edad_calculada} años.")
                break
            else:
                print("Formato de fecha incorrecto. Use el formato correcto (YYYY-MM-DD).")
        
        registro["ocupacion"] = solicitar_campo("Nueva ocupación", "ocupacion")
        registro["empresa"] = solicitar_campo("Nueva empresa", "empresa")
        registro["tipo_contrato"] = solicitar_campo("Nuevo tipo de contrato", "tipo_contrato")
        registro["es_asegurado"] = solicitar_campo("Es asegurado/a (sí/no)", "es_asegurado")
        registro["tipo_sangre"] = solicitar_campo("Nuevo tipo de sangre", "tipo_sangre")
        registro["direccion"] = solicitar_campo("Nueva dirección", "direccion")
        registro["telefono_residencial"] = solicitar_campo("Nuevo teléfono residencial", "telefono_residencial")
        registro["telefono_celular"] = solicitar_campo("Nuevo teléfono celular", "telefono_celular")

        guardar_datos(datos)

        print("-" * 50)
        print(f"\nRegistro con ID {id_a_actualizar} actualizado con éxito.")

    else:
        print(f"\nError: No se encontró ningún registro con ID {id_a_actualizar}.")


def eliminar_registros():
    """Solicita un ID y elimina el registro correspondiente del CSV."""
    datos = obtener_datos()

    print("\n--------- Eliminar registro por ID ---------")
    if not datos:
        print("-" * 50)
        print("No hay registros para eliminar.")
        return

    id_a_eliminar = input("Digite el ID del registro que desea eliminar: ")
    
    # Crear una nueva lista excluyendo el registro con el ID a eliminar
    datos_antes = len(datos)
    datos_actualizados = [persona for persona in datos if persona.get("id") != id_a_eliminar]
    datos_despues = len(datos_actualizados)

    print("-" * 50)

    if datos_antes > datos_despues:
        # Se encontró y eliminó el registro
        guardar_datos(datos_actualizados)
        print(f"\nRegistro con ID {id_a_eliminar} eliminado con éxito.")
    else:
        # El registro no fue encontrado
        print(f"\nError: No se encontró ningún registro con ID {id_a_eliminar}. No se realizó ninguna eliminación.")


def menu_principal():
    #Inciando la función que crea el archivo csv, donde se guardarán los datos.
    inicializar_csv()
    
    #Muestra en pantalla un mensaje de bienvenida al programa.
    print("-" * 50)
    print("Bienvenido/a al programa de registro de personas.")
    while True:
        print("-" * 50)
        print("\n¿Qué desea hacer?")
        print("-" * 50)
        print("1. Crear nuevo registro")
        print("2. Mostrar todos los registros")
        print("3. Actualizar registro por ID")
        print("4. Eliminar registro por ID")
        print("5. Salir")
        print("-" * 50)

        opcion = input("Favor de digitar una de las opciones: ")

        if (opcion == "1"):
            crear_registros()
        elif (opcion == "2"):
            leer_registros()
        elif (opcion == "3"):
            actualizar_registros()
        elif (opcion == "4"):
            eliminar_registros()
        elif (opcion == "5"):
            print("-" * 50)
            print("Muchas gracias por utilizar nuestros servicios.")
            print("JotasCode © 2025 (all rights reserved).")
            print("-" * 50)
            break
        else:
            print("Opcición no valida, favor de registrar una de las opciones indicadas.")

if __name__ == "__main__":
    menu_principal()