import pandas as pd

try:
    df = pd.read_json('1_titanic.jsonl', orient='records') 
   
    df.to_csv('4_titanic.csv', index=False) 
    
    print("✅ Conversión exitosa: 1_titanic.jsonl -> 4_titanic.csv")

except FileNotFoundError:
    print("❌ Error: El archivo '1_titanic.jsonl' no fue encontrado.")