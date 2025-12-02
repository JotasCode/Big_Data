import pandas as pd
import sqlite3

try:
    df = pd.read_csv('titanic.csv')
    
    conn = sqlite3.connect('2_titanic.db')

    df.to_sql('tabla_desde_csv', conn, if_exists='replace', index=False)
    
    conn.close()
    
    print("✅ Conversión exitosa: titanic.csv -> tabla_desde_csv en 2_titanic.db")

except FileNotFoundError:
    print("❌ Error: El archivo 'titanic.csv' no fue encontrado.")
except Exception as e:
    print(f"❌ Ocurrió un error al convertir a SQL: {e}")