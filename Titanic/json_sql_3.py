import pandas as pd

def from_json_to_sql(json_name, sql_name, table_name):
    try:
        df = pd.read_json(json_name)

        columns = df.columns
        create_cols = ', '.join([f'"{col}"' for col in df.columns])
        create_sql = f"CREATE TABLE {table_name} ({create_cols});\n\n"

        insert_lines = []
        
        for _, row in df.iterrows():
            values = []
            for val in row:
                if pd.isna(val):
                    values.append('NULL')
                else:
                    text = str(val).replace("'", "''")
                    values.append(f'{text}')

            columns_sql = ", ".join([f'"{col}"' for col in columns])
            values_sql = ", ".join(values)

            insert_lines.append( f"INSERT INTO {table_name} ({columns_sql}) VALUES ({values_sql});")

        with open(sql_name, "w", encoding="utf-8") as f:
            f.write(create_sql)
            f.write("\n".join(insert_lines))

        print(f"✅ Los datos del archivo {json_name} pasaron al archivo {sql_name} de forma exitosa.")

    except FileNotFoundError:
        print(f"❌ Error: El archivo {json_name} no fue encontrado.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar crear el archivo {sql_name}: {e}")