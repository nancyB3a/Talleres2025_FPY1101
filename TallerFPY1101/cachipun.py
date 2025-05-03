import random as r
print('*.*'*15)
print('\t\tCACHIPÚN')
print('*.*'*15)
print('1.- Piedra')
print('2.- Papel')
print('3.- Tijera')
turnoJugador = int(input('Que eliges?: '))
turnoPs5 = r.randint(1,3) #número aleatorio entre 1 y 3
print('PS5 eligió:', turnoPs5)
#resuelvo el cachipún con las condiciones posibles
#primero cuando gana jugador
if turnoPs5 == 1 and turnoJugador == 2:
    print('GANASTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 2 and turnoJugador == 3:
    print('GANASTE')
    print('Tijera corta papel')
elif turnoPs5 == 3 and turnoJugador == 1:
    print('GANASTE')
    print('Piedra aplasta tijera')
#luego cuando pierde el jugador
elif turnoPs5 == 1 and turnoJugador == 3:
    print('PERDISTE')
    print('Piedra aplasta tijera')
elif turnoPs5 == 2 and turnoJugador == 1:
    print('PERDISTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 3 and turnoJugador == 2:
    print('PERDISTE')
    print('Tijera corta papel')
else:
    print('EMPATE')