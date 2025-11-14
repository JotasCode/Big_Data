#Javier José Jiménez Soto
#Actividad #8
print("Actividad #8 - Trabajando con Archivos")

import csv
import os
from tabulate import tabulate

ARCHIVO_CSV = "informacion.csv"
CAMPOS = [
    "nombre", "apellido", "sexo", "edad",
]

def crear_csv():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo: 
            writer = csv.DictWriter(archivo, fieldnames=CAMPOS)
            writer.writeheader()
            print(f"Archivo '{ARCHIVO_CSV}' creado con éxito.")

def menu():
    crear_csv()

if __name__ == "__main__":
    menu()