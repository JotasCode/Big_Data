import csv
import os
from datetime import date, datetime
from tabulate import tabulate

ARCHIVO_CSV = "registro_personas.csv"
CAMPOS = [
    "id", "nombre_producto", "nombre_compañia","fecha_ingreso","tipo_producto", "fecha_exp"
]

def calcular_exp(fecha_ingreso_str):
    try:
        fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d").date()
    except ValueError:
        return None 

    hoy = date.today()

    tiempo_exp = hoy.year - fecha_ingreso.year 

    if(hoy.month, hoy.day) < (fecha_ingreso.month, fecha_ingreso.day):
        edad -= 1 

    return edad 