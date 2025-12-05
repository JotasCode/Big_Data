import pandas 
from csv_json_1 import from_csv_to_json as csv_json 
from csv_sql_2 import from_csv_to_sql as csv_sql
from json_sql_3 import from_json_to_sql as json_sql
from json_csv_4 import from_json_to_csv as json_csv

while True:
    print('---------- Opciones ----------')
    print('1. Pasar datos de la tripulación del Titanic de un archivo csv a un archivo json.')
    print('2. Pasar datos de la tripulación del Titanic de un archivo csv a un archivo sql.')
    print('3. Pasar datos de la tripulación del Titanic de un archivo json a un archivo sql.')
    print('4. Pasar datos de la tripulación del Titanic de un archivo json a un archivo csv.')
    print('5. Salir')

    selection = input('Elija el número de la acción que desea realizar: ')

    if selection == '1':
        csv_json('titanic.csv', '1_titanic.json')
    elif selection == '2':
        csv_sql('titanic.csv', '2_titanic.sql', 'tabla_pasajeros')
    elif selection == '3':
        json_sql('1_titanic.json', '3_titanic.sql', 'pasajeros')
    elif selection == '4':
        json_csv('1_titanic.json', '4_titanic.csv')
    elif selection == '5':
        print('Hasta la próxima.')
        break
    else:
        print('Opción invalida, seleccione el número de la oopción que desea elejir.')