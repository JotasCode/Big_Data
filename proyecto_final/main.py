import csv
import os
from datetime import date, datetime
from tabulate import tabulate

ARCHIVO_CSV = "inventario.csv"
COLUMNAS = [
    "id", "nombre_producto", "compañía_producto", "tipo_producto", "peso_producto(gramos)", "fecha_ingreso", "fecha_exp", "tiempo_exp(días)"
]

def calcular_dias_restantes(fecha_exp_str):
    try:
        fecha_exp = datetime.strptime(fecha_exp_str, "%Y-%m-%d").date()
    except ValueError:
        return None 

    hoy = date.today()

    dias_restantes = (fecha_exp - hoy).days

    return dias_restantes

def iniciar_csv():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo: 
            writer = csv.DictWriter(archivo, fieldnames=COLUMNAS)
            writer.writeheader()
            print(f"Archivo '{ARCHIVO_CSV}' creado con éxito.")

def obtener_datos():
    datos = []

    try:
        with open(ARCHIVO_CSV, "r", newline= "", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                datos.append(fila)

    except FileNotFoundError:
        pass  

    return datos

def guardar_datos(datos):
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=COLUMNAS)
        writer.writeheader()
        writer.writerows(datos)

def obtener_siguiente_id(datos):
    if not datos:
        return 1

    max_id = max(int(persona["id"]) for persona in datos if persona["id"].isdigit())

    return max_id + 1

def crear_productos():
    iniciar_csv()

    datos = obtener_datos()
    nuevo_id = obtener_siguiente_id(datos)

    print("\n--------- Insertando nuevo producto ---------")
    registro = {
        "id" : str(nuevo_id)
    }
    
    registro["nombre_producto"] = input("Escriba el nombre del producto: ")
    registro["compañía_producto"] = input("Escriba el nombre de la compañía del producto: ")
    registro["tipo_producto"] = input("Escriba el tipo del producto: ")
    registro["peso_producto(gramos)"] = input("Escriba el peso del producto (en gramos): ")
    registro["fecha_ingreso"] = input("Escriba la fecha en la que se ingresó el producto (YYYY-MM-DD): ")
    
    while True:
        fecha_exp_str = input("Fecha de esxpiración del producto (YYYY-MM-DD): ")
        dias_restantes = calcular_dias_restantes(fecha_exp_str)

        if dias_restantes is not None:
            registro["fecha_exp"] = fecha_exp_str
            registro["tiempo_exp(días)"] = str(dias_restantes)
            
            if dias_restantes >= 0:
                print(f"Tiempo restante del producto: {dias_restantes} días.")
            else:
                print(f"¡ADVERTENCIA! Producto expirado hace {-dias_restantes} días.")
            
            break
        else:
            print("Formato de fecha incorrecto. Use el formato correcto (YYYY-MM-DD).")

    datos.append(registro)
    guardar_datos(datos)

    print("-" * 50)
    print(f"\nProducto con el id {nuevo_id} creado y guardado con éxito.")

def leer_productos():
    datos = obtener_datos()

    print("\n--------- Productos registrados: ---------")
    if datos:
        print(tabulate(datos, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nNo hay productos registrados para mostrar. Use la opción 1 para registrar uno.")

def actualizar_productos():
    datos = obtener_datos()

    print("\n--------- Actualizar productos por ID ---------")
    if not datos:
        print("No hay productos para actualizar.")
        return

    id_a_actualizar = input("Digite el ID del producto que desea actualizar: ")
    
    indice_encontrado = -1
    for i, producto in enumerate(datos):
        if producto.get("id") == id_a_actualizar:
            indice_encontrado = i
            break
            
    if indice_encontrado != -1:
        registro = datos[indice_encontrado]
        print("-" * 50)
        print(f"Producto encontrado (ID: {id_a_actualizar}). (Deje la columna vacía para mantener el valor actual).")
        print("-" * 50)

        def solicitar_columna(prompt, key):
            nuevo_valor = input(f"{prompt} (Actual: {registro.get(key, 'N/A')}): ").strip()
            return nuevo_valor if nuevo_valor else registro.get(key, "")

        registro["nombre_producto"] = solicitar_columna("Nuevo nombre de producto", "nombre_producto")
        registro["compañía_producto"] = solicitar_columna("Nueva compañía de producto", "compañía_producto")
        registro["tipo_producto"] = solicitar_columna("Nuevo tipo de producto", "tipo_producto")
        registro["peso_producto(gramos)"] = solicitar_columna("Nuevo peso del producto (en gramos)", "peso_producto(gramos)")
        registro["fecha_ingreso"] = solicitar_columna("Nueva fecha de ingreso", "fecha_ingreso")

        fecha_exp_actual = registro.get("fecha_exp(días)", "")
        while True:
            nueva_fecha_exp_str = input(f"Nueva fecha de expiración (YYYY-MM-DD) (Actual: {fecha_exp_actual}): ").strip()
            
            if not nueva_fecha_exp_str:
                dias_restantes = calcular_dias_restantes(fecha_exp_actual)
                registro["tiempo_exp(días)"] = str(dias_restantes)
                print(f"Días restantes recalculados: {dias_restantes} días.")
                break
            
            dias_restantes = calcular_dias_restantes(nueva_fecha_exp_str)

            if dias_restantes is not None:
                registro["fecha_exp"] = nueva_fecha_exp_str
                registro["tiempo_exp(días)"] = str(dias_restantes)
                print(f"Días restantes actuales: {dias_restantes}.")
                break
            else:
                print("Formato de fecha incorrecto. Use el formato correcto (YYYY-MM-DD).")
        
        guardar_datos(datos)

        print("-" * 50)
        print(f"\nProducto con ID {id_a_actualizar} actualizado con éxito.")

    else:
        print(f"\nError: No se encontró ningún producto con ID {id_a_actualizar}.")

def eliminar_productos():
    datos = obtener_datos()

    print("\n--------- Eliminar producto por ID ---------")
    if not datos:
        print("-" * 50)
        print("No hay productos para eliminar.")
        return

    id_a_eliminar = input("Digite el ID del producto que desea eliminar: ")
    
    datos_antes = len(datos)
    datos_actualizados = [producto for producto in datos if producto.get("id") != id_a_eliminar]
    datos_despues = len(datos_actualizados)

    print("-" * 50)

    if datos_antes > datos_despues:
        guardar_datos(datos_actualizados)
        print(f"\nProducto con ID {id_a_eliminar} eliminado con éxito.")
    else:
        print(f"\nError: No se encontró ningún producto con ID {id_a_eliminar}. No se realizó ninguna eliminación.")

def menu_principal():
    iniciar_csv()
    
    print("-" * 50)
    print("Bienvenido(a) al programa de registro de productos.")
    while True:
        print("-" * 50)
        print("\n¿Qué desea hacer?")
        print("-" * 50)
        print("1. Registrar nuevo producto")
        print("2. Mostrar todos los productos")
        print("3. Cambiar datos de producto por ID")
        print("4. Eliminar producto por ID")
        print("5. Salir")
        print("-" * 50)

        opcion = input("Favor de digitar una de las opciones: ")

        if (opcion == "1"):
            crear_productos()
        elif (opcion == "2"):
            leer_productos()
        elif (opcion == "3"):
            actualizar_productos()
        elif (opcion == "4"):
            eliminar_productos()
        elif (opcion == "5"):
            print("-" * 50)
            print("Muchas gracias por utilizar nuestros servicios.")
            print("Atlantida © 2025 (all rights reserved).")
            print("-" * 50)
            break
        else:
            print("Opcición no valida, favor de registrar una de las opciones indicadas.")

if __name__ == "__main__":
    menu_principal()