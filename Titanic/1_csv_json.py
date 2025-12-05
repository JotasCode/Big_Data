import pandas as pd

def from_csv_to_json(csv_name, json_name):
    try:
        df = pd.read_csv(csv_name) 

        df.to_json(json_name, orient='records', indent=2) 
        
        print(f"✅ Los datos del archivo {csv_name} pasaron al archivo {json_name} de forma exitosa.")
        
    except FileNotFoundError:
        print(f"❌ Error: El archivo {csv_name} no fue encontrado.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar crear el archivo {json_name}: {e}")

from_csv_to_json('titanic.csv', '1_titanic.json')