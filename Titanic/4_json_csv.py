import pandas as pd

def from_json_to_csv(json_name, csv_name):
    try:
        df = pd.read_json(json_name) 
    
        df.to_csv(csv_name, index=False) 
        
        print(f"✅ Los datos del archivo {json_name} pasaron al archivo {csv_name} de forma exitosa.")

    except FileNotFoundError:
        print(f"❌ Error: El archivo {json_name} no fue encontrado.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar crear el archivo {csv_name}: {e}")

from_json_to_csv('1_titanic.json', '4_titanic.csv')