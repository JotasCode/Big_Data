#Javier José Jiménez Soto
#Actividad #9
print("Actividad #9 - Estructuras de Datos Nativas")

edad = int(input("Escriba su edad: "))

if (edad < 0):
    print("Aún no has nacido.")
elif(edad >= 0 and edad <= 12):
    print("Eres un(a) niño(a).")
elif(edad >= 13 and edad <= 17):
    print("Eres un(a) adolescente.")
elif(edad >= 18 and edad <= 100):
    print("Eres un(a) adulto.")
else:
    print("Tienes una edad cuestionable.")
print("---------------------------------")

print("Fin del programa.")