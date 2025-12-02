import pandas as pd
import sqlite3

try:
    df = pd.read_json('1_titanic.jsonl')
    
    conn = sqlite3.connect('3_titanic.db')
 
    df.to_sql('tabla_desde_json', conn, if_exists='replace', index=False)

    conn.close()
    
    print("✅ Conversión exitosa: 1_titanic.jsonl -> tabla_desde_json en 3_titanic.db")

except FileNotFoundError:
    print("❌ Error: El archivo '1_titanic.jsonl' no fue encontrado.")
except Exception as e:
    print(f"❌ Ocurrió un error al convertir a SQL: {e}")