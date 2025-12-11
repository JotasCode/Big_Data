class Futbolista:
    def __init__(self, nombre, apellido, sobrenombre, sexo, fecha_nacimiento, edad, estado, altura, peso, nacionalidad, posición, equipo, número_equipo, seleción, número_seleción, velocidad, aceleración, estamina, fuerza, velocidad_disparo, precisión_disparo, agilidad, agilidad_balón, recepción_balón, control_balón, control_balón_cabeza, altura_salto, debút_profesional, partidos_jugados, goles, asistencias, trofeos, premios_individuales, tipo_celebración, patrocinadores, salario_anual):

        self.nombre = nombre
        self.apellido = apellido
        self.sobrenombre = sobrenombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.estado = estado
        self.altura = altura 
        self.peso = peso 
        self.nacionalidad = nacionalidad

        self.posición = posición
        self.equipo = equipo
        self.número_equipo = número_equipo
        self.seleción = seleción
        self.número_seleción = número_seleción

        self.velocidad = velocidad 
        self.aceleración = aceleración
        self.estamina = estamina
        self.fuerza = fuerza
        self.velocidad_disparo = velocidad_disparo
        self.precisión_disparo = precisión_disparo
        self.agilidad = agilidad
        self.agilidad_balón = agilidad_balón
        self.recepción_balón = recepción_balón
        self.control_balón = control_balón
        self.control_balón_cabeza = control_balón_cabeza
        self.altura_salto = altura_salto
        self.debút_profesional = debút_profesional
        self.partidos_jugados = partidos_jugados
        self.goles = goles
        self.asistencias = asistencias
        self.trofeos = trofeos
        self.premios_individuales = premios_individuales
        self.tipo_celebración = tipo_celebración
        self.patrocinadores = patrocinadores
        self.salario_anual = salario_anual

    def correr(self):
        print(f'{self.nombre} está corriendo a una velocidad de {self.velocidad} con una aceleración de {self.aceleración}.')

    def disparar(self):
        print(f'{self.nombre} está disparando el balón a un velocidad de {self.velocidad_disparo} con una precisión de {self.precisión_disparo}.')

    def desllizarse(self):
        print(f'{self.nombre} está deslizandose.')

    def defender(self):
        print(f'{self.nombre} está defendiendo.')

    def driblear(self):
        print(f'{self.nombre} está dribleando con el balón.')

    def saltar(self):
        print(f'{self.nombre} está saltando a una altura de {self.altura_salto} a una velocidad de {self.velocidad} con una aceleración de {self.aceleración}.')

    def cabecear(self):
        print(f'{self.nombre} está cabeceando.')

    def pasar(self):
        print(f'{self.nombre} está pasando el balón a un velocidad de {self.velocidad_disparo} con una precisión de {self.precisión_disparo}.')

 Messi = Futbolista('Lionel Andrés', 'Messi Cuccittini', 'La Pulga', 'macho', '24/6/1987', '38 años', 'activo', '1.70m', '72kg', 'argentina, española e italiana', 'extremo derecho', 'Inter de Miami', '10', 'argentina', '10', '30km/h', '5m/s^2', 'promedio', 'mala', '85km/h', '80%', 'buena', 'muy buena', 'muy buena', 'muy bueno', 'malo', '30 cm', '16/10/2004', 1137, 896, 409, 48, 60, 'Señalar al Cielo', ['Adidas', 'Pepsi', 'Gatorade'], '50,000,000 dolares')