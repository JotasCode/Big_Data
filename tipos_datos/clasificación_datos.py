entrada_datos = input("Digite algo: ")

print("Usted digitó: ", entrada_datos)

if entrada_datos.lstrip("-").isdigit():
    número = int(entrada_datos)
    if número < 0:
        print("Usted digitó un número entero negativo.")
    elif número > 0:
        print("Usted digitó un número entero positivo.")
    else:
        print("Usted digitó cero.")
        
elif "." in entrada_datos and entrada_datos.replace(".", "", 1).isdigit():
    print("Usted digitó un número decimal.")
    
elif entrada_datos.lower() == "false":
    print("Usted digitó un dato booleano falso.")
    
elif entrada_datos.lower() == "true":
    print("Usted digitó un dato booleano verdadero.")
    
else:
    if entrada_datos.isalpha():
        print("Usted digitó un texto con solo letras.")
    else:
        print("Usted digitó un texto con símbolos, espacios y/o números.")