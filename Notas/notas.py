from datetime import date 

class CalculadoraEdad:

    def.fecha_nacimiento = date(anio_nacimiento, mes_nacimiento, dia_nacimiento)

    return self.fecha_nacimiento

    def calcular_edad(self):
    hoy = date.today()
    edad = hoy.year - self.fecha_nacimiento.year

    if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
        edad -= 1

    return edad

anio = 1990
mes = 5
dia = 15

persona1 = CalculadoraEdad(anio, mes, dia)
edd_actual = persona1.calcular_edad()

print(f"Fecha de nacimiento: {anio}-{mes:02d}-{dia:02d}")
print(f"La edad actual es: {edad_actual} años.")


hoy = date.today()
anio_ejemplo = hoy.year - 30 
mes_ejemplo = hoy.month
dia_ejemplo = hoy.day

persona2 = CalculadoraEdad{anio_ejemplo, mes_ejemplo, dia_ejemplo}
edad_ejemplo = persona2.calcular_edad()

print("-" * 20)
print(f"Fecha de nacimiento {ejemplo 2}: {anio_ejemplo}-{mes_ejemplo:02d}-{dia_ejemplo:02d}")
print(f"La edad actual es: {edad_ejemplo} años.")