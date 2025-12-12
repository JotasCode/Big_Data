from futbolistas import messi, cristiano, neymar

while True:
    print('---------- Jugadores ----------')
    print('a = Messi')
    print('b = Crstiano')
    print('c = Neymar')

    election = input('Elija un jugador: ')
    if election == 'a':
        election = messi
        break
    elif election == 'b':
        election = cristiano
        break
    elif election == 'c':
        election = neymar
        break
    else:
        print('Opción invalida.')


while True:
    print('---------- Opciones ----------')
    print('a = correr')
    print('s = deslizarse')
    print('d = defender')
    print('f = driblear')
    print('g = cabecear')
    print('h = saltar')
    print('j = disparar')
    print('k = pasar el balón')
    print('l = celebrar')
    print('ñ = salir')
    selection = input('Selecione una opción: ')

    if selection == 'a':
        election.correr()
    elif selection == 's':
        election.deslizarse()
    elif selection == 'd':
        election.defender()
    elif selection == 'f':
        election.driblear()
    elif selection == 'g':
        election.cabecear()
    elif selection == 'h':
        election.saltar()
    elif selection == 'j':
        election.disparar()
    elif selection == 'k':
        election.pasar()
    elif selection == 'l':
        election.celebrar()
    elif selection == 'ñ':
        break
    else:
        print('Opción invalida.')