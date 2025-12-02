import pandas as pd

try:
    df = pd.read_csv('titanic.csv') 

    df.to_json('1_titanic.jsonl', orient='records', lines=True) 
    
    print("✅ Conversión exitosa: titanic.csv -> 1_titanic.json")
    
except FileNotFoundError:
    print("❌ Error: El archivo 'titanic.csv' no fue encontrado.")