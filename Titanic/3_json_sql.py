import pandas as pd

def generate_insert_statements(df, table_name):
    inserts = []
    columns = ', '.join([f'"{col}"' for col in df.columns])
    
    for index, row in df.iterrows():
        values_list = []
        for val in row.values:
            if pd.notna(val):
                escaped_value = str(val).replace("'", "''")
                values_list.append(f"'{escaped_value}'")
            else:
                values_list.append('NULL')

        values = ', '.join(values_list)
        inserts.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
    return inserts

try:
    df = pd.read_json('1_titanic.json', orient='records')

    sql_inserts = generate_insert_statements(df, 'mi_tabla_json')

    with open('3_titanic.sql', 'w', encoding='utf-8') as f:
        f.write(f"CREATE TABLE mi_tabla_json ({', '.join([f'{col} TEXT' for col in df.columns])});\n")
        f.write('\n'.join(sql_inserts))

    print("✅ Conversión de JSON a instrucciones SQL completada.")

except FileNotFoundError:
    print("❌ Error: El archivo '1_titanic.json' no fue encontrado. Asegúrate de que esté en la misma carpeta.")
    
except Exception as e:
    print(f"❌ Ocurrió un error al intentar crear el archivo 3_titanic.sql: {e}")