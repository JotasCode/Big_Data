from datetime import date

class CalcularFecha:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.fecha_nacimiento = date(self.year, self.month, self.day)

        return self.fecha_nacimiento
    
fecha_javier = CalcularFecha(2006, 8, 3)
print(fecha_javier)