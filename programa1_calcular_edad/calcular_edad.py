print("Bienvenido/a al programa de estados de uns er humano.")
print("Desarrollado por Javier Jiménez.")
print("--------------------------------")

edad = int(input("Escriba su edad: "))

if (edad < 0):
    print("Aún no has nacido.")
elif(edad >= 0 and edad <= 3):
    print("Eres un bebé.")
elif(edad >= 4 and edad <= 12):
    print("Eres un/a niño/a.")
elif(edad >= 13 and edad <= 17):
    print("Eres un/a adolescente.")
elif(edad >= 18 and edad <= 29):
    print("Eres un/a adult/a joven.")
elif(edad >= 30 and edad <= 39):
    print("Eres un/a adulto/a con experiencia.")
elif(edad >= 40 and edad <= 59):
    print("Eres un/a adulto/a mayor.")
elif(edad >= 60 and edad <= 99):
    print("Eres un/a anciano/a.")
else:
    print("Tienes una edad cuestionable.")
print("---------------------------------")

print("Fin del programa.")