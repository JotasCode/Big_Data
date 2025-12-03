import pandas as pd
from sqlalchemy import create_engine

try:
    df = pd.read_csv('titanic.csv')

    engine = create_engine('sqlite:///:memory:')

    df.to_sql('nombre_tabla', con=engine, if_exists='replace', index=False)

    def generate_insert_statements(df, table_name):
        inserts = []
        columns = ', '.join([f'"{col}"' for col in df.columns])
        for index, row in df.iterrows():
            values = ', '.join([
                f"'{str(val).replace("'", "''")}'" if pd.notna(val) else 'NULL'
                for val in row.values
            ])
            inserts.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
        return inserts

    sql_inserts = generate_insert_statements(df, 'tabla_pasajeros')

    with open('2_titanic.sql', 'w', encoding='utf-8') as f:
        f.write(f"CREATE TABLE tabla_pasajeros ({', '.join([f'{col} TEXT' for col in df.columns])});\n")
        f.write('\n'.join(sql_inserts))

    print("✅ Conversión de CSV a instrucciones SQL completada.")

except FileNotFoundError:
    print("❌ Error: El archivo 'titanic.csv' no fue encontrado.")
except Exception as e:
    print(f"❌ Ocurrió un error al intentar crear el archivo 2_titanic.sql: {e}")