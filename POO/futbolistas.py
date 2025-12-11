class Futbolista:
    def __init__(self, nombre, apellido, apodo, sexo, fecha_nacimiento, edad, estado, altura, peso, nacionalidad, posición, equipo, número_equipo, seleción, número_seleción, velocidad_kmh, aceleración_ms2, estamina, fuerza, velocidad_disparo_kmh, precisión_disparo, agilidad, recepción_balón, control_balón, control_balón_cabeza, altura_salto_cm, debút_profesional, partidos_jugados, goles, asistencias, trofeos, premios_individuales, tipo_celebración, patrocinadores, salario_anual):

        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
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

        self.velocidad_kmh = velocidad_kmh 
        self.aceleración_ms2 = aceleración_ms2
        self.estamina = estamina
        self.fuerza = fuerza
        self.velocidad_disparo_kmh = velocidad_disparo_kmh
        self.precisión_disparo = precisión_disparo
        self.agilidad = agilidad
        self.recepción_balón = recepción_balón
        self.control_balón = control_balón
        self.control_balón_cabeza = control_balón_cabeza
        self.altura_salto_cm = altura_salto_cm
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
        if self.velocidad_kmh >= 35:
            print(f'{self.apodo} está corriendo muy rápido.')
        elif self.velocidad_kmh >= 30:
            print(f'{self.apodo} está corriendo rápido.')
        elif self.velocidad_kmh >= 25:
            print(f'{self.apodo} está corriendo a una velocidad promedio.')
        elif self.velocidad_kmh >= 20:
            print(f'{self.apodo} está corriendo lento.')
        else:
            print(f'{self.apodo} está corriendo muy lento.')

    def disparar(self):
        if self.velocidad_disparo_kmh >= 130:
            print(f'{self.apodo} está disparando muy fuerte.')
        elif self.velocidad_disparo_kmh >= 115:
            print(f'{self.apodo} está disparando fuerte.')
        elif self.velocidad_disparo_kmh >= 100:
            print(f'{self.apodo} está disparando con una fuerza promedio.')
        elif self.velocidad_disparo_kmh >= 85:
            print(f'{self.apodo} está disparando débil.')
        else:
            print(f'{self.apodo} está disparando muy débil.')

        if self.precisión_disparo >= 95:
            print('Con una precisión muy buena.')
        elif self.precisión_disparo >= 90:
            print('Con una buena precisión.')
        elif self.precisión_disparo >= 85:
            print('Con una precisión promedio.')
        elif self.precisión_disparo >= 80:
            print('Con una mala precisión.')
        else:
            print('Con una precisión muy buena.')
    
    def deslizarse(self):
        print(f'{self.apodo} está deslizandose.')

    def defender(self):
        if self.fuerza == 'muy buena':
            print(f'{self.apodo} está defendiendo muy bien.')
        elif self.fuerza == 'buena':
            print(f'{self.apodo} está defendiendo bien.')
        elif self.fuerza == 'promedio':
            print(f'{self.apodo} está defendiendo de forma efectiva.')
        elif self.fuerza == 'mala':
            print(f'{self.apodo} está defendiendo mal.')
        elif self.fuerza == ' muy mala':
            print(f'{self.apodo} está defendiendo muy mal.')
        else:
            print(f'{self.apodo} no está defendiendo.')

    def driblear(self):
        print(f'{self.apodo} está dribleando con el balón.')

    def saltar(self):
        print(f'{self.apodo} está saltando a una altura de {self.altura_salto_cm}cm, a una velocidad de {self.velocidad_kmh}km/h, con una aceleración de {self.aceleración_ms2}m/s^2.')

    def cabecear(self):
        print(f'{self.apodo} está cabeceando.')

    def pasar(self):
        if self.velocidad_disparo_kmh >= 130:
            print(f'{self.apodo} está pasando el balón muy fuerte.')
        elif self.velocidad_disparo_kmh >= 115:
            print(f'{self.apodo} está pasando el balón fuerte.')
        elif self.velocidad_disparo_kmh >= 100:
            print(f'{self.apodo} está pasando el balón con una fuerza promedio.')
        elif self.velocidad_disparo_kmh >= 85:
            print(f'{self.apodo} está pasando el balón débil.')
        else:
            print(f'{self.apodo} está pasando el balón muy débil.')
        
        if self.precisión_disparo >= 95:
            print('Con una precisión muy buena.')
        elif self.precisión_disparo >= 90:
            print('Con una buena precisión.')
        elif self.precisión_disparo >= 85:
            print('Con una precisión promedio.')
        elif self.precisión_disparo >= 80:
            print('Con una mala precisión.')
        else:
            print('Con una precisión muy buena.')

    def celebrar(self):
        print(f'{self.apodo} está haciendo su iconica celebración de {self.tipo_celebración}.')

messi = Futbolista(
    nombre = 'Lionel Andrés', 
    apellido = 'Messi Cuccittini', 
    apodo = 'La Pulga', 
    sexo = 'hombre', 
    fecha_nacimiento = '24/6/1987', 
    edad = '38 años', 
    estado = 'activo', 
    altura = '1.70m', 
    peso = '72kg', 
    nacionalidad = ['argentina', 'española' 'italiana'], 
    posición = 'extremo derecho', 
    equipo = 'Inter de Miami', 
    número_equipo = '10', 
    seleción = 'argentina', 
    número_seleción = '10', 
    velocidad_kmh = 28, 
    aceleración_ms2 = 5, 
    estamina = 'promedio', 
    fuerza = 'mala', 
    velocidad_disparo_kmh = 116, 
    precisión_disparo = 90, 
    agilidad = 'buena', 
    recepción_balón = 'muy buena', 
    control_balón = 'muy bueno', 
    control_balón_cabeza = 'malo', 
    altura_salto_cm = 30, 
    debút_profesional = '16/10/2004',
    partidos_jugados = 1137, 
    goles = 896, 
    asistencias = 409, 
    trofeos = 48, 
    premios_individuales = 60, 
    tipo_celebración = 'Señalar al Cielo', 
    patrocinadores = ['Adidas', 'Pepsi', 'Gatorade'], 
    salario_anual = '50,000,000 dolares'
    )

print('-' * 80)
messi.correr()
messi.disparar()
messi.deslizarse()
messi.defender()
messi.driblear()
messi.saltar()
messi.cabecear()
messi.pasar()
messi.celebrar()
print('-' * 80)

cristiano = Futbolista(
    nombre = 'Cristiano', 
    apellido = 'Ronaldo', 
    apodo = 'El Bicho', 
    sexo = 'hombre', 
    fecha_nacimiento = '5/2/1985', 
    edad = '40 años', 
    estado = 'activo', 
    altura = '1.87m', 
    peso = '83kg', 
    nacionalidad = 'portuguesa', 
    posición = 'delantero centro', 
    equipo = 'Al-Nassar', 
    número_equipo = '7', 
    seleción = 'portuguesa', 
    número_seleción = '7', 
    velocidad_kmh = 30, 
    aceleración_ms2 = 4.5, 
    estamina = 'promedio', 
    fuerza = 'mala', 
    velocidad_disparo_kmh = 117, 
    precisión_disparo = 85, 
    agilidad = 'mala',  
    recepción_balón = 'promedio', 
    control_balón = 'bueno', 
    control_balón_cabeza = 'malo', 
    altura_salto_cm = 60, 
    debút_profesional = '20/8/2003',
    partidos_jugados = 1137, 
    goles = 896, 
    asistencias = 409, 
    trofeos = 48, 
    premios_individuales = 60, 
    tipo_celebración = 'SIIIIUUUU', 
    patrocinadores = ['Adidas', 'Pepsi', 'Gatorade'], 
    salario_anual = '50,000,000 dolares'
    )

print('-' * 80)
cristiano.correr()
cristiano.disparar()
cristiano.deslizarse()
cristiano.defender()
cristiano.driblear()
cristiano.saltar()
cristiano.cabecear()
cristiano.pasar()
cristiano.celebrar()
print('-' * 80)