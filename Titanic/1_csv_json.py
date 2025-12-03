import pandas as pd

def from_csv_to_json(nombre_archivo):
    try:
        df = pd.read_csv('titanic.csv') 

        df.to_json(nombre_archivo, orient='records', indent=4) 
        
        print("✅ Conversión exitosa: titanic.csv -> 1_titanic.json")
        
    except FileNotFoundError:
        print("❌ Error: El archivo 'titanic.csv' no fue encontrado.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar crear el archivo 1_titanic.json: {e}")

from_csv_to_json('1_titanic.json')