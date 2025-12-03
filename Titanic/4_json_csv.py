import pandas as pd

def from_json_to_csv(archivo_csv):
    try:
        df = pd.read_json('1_titanic.json', orient='records') 
    
        df.to_csv(archivo_csv, index=False) 
        
        print("✅ Conversión exitosa: 1_titanic.json -> 4_titanic.csv")

    except FileNotFoundError:
        print("❌ Error: El archivo '1_titanic.json' no fue encontrado.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar crear el archivo 4_titanic.sql: {e}")

from_json_to_csv('4_titanic.csv')