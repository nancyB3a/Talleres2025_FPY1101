import random as r
jugadorGana = 0
ps5Gana = 0
print('*.*'*15)
print('\t\tCACHIPÚN')
print('*.*'*15)
print("""1.- Piedra
2.- Papel
3.- Tijera""")

turnoJugador = int(input('Que eliges?: '))
turnoPs5 = r.randint(1,3) #número aleatorio entre 1 y 3
print('PS5 eligió:', turnoPs5)
#resuelvo el cachipún con las condiciones posibles
#primero cuando gana jugador
if turnoPs5 == 1 and turnoJugador == 2:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 2 and turnoJugador == 3:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Tijera corta papel')
elif turnoPs5 == 3 and turnoJugador == 1:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Piedra aplasta tijera')
#luego cuando pierde el jugador
elif turnoPs5 == 1 and turnoJugador == 3:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Piedra aplasta tijera')
elif turnoPs5 == 2 and turnoJugador == 1:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 3 and turnoJugador == 2:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Tijera corta papel')
else:
    print('EMPATE')
#segunda jugada
turnoJugador = int(input('Que eliges?: '))
turnoPs5 = r.randint(1,3) #número aleatorio entre 1 y 3
print('PS5 eligió:', turnoPs5)
#resuelvo el cachipún con las condiciones posibles
#primero cuando gana jugador
if turnoPs5 == 1 and turnoJugador == 2:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 2 and turnoJugador == 3:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Tijera corta papel')
elif turnoPs5 == 3 and turnoJugador == 1:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Piedra aplasta tijera')
#luego cuando pierde el jugador
elif turnoPs5 == 1 and turnoJugador == 3:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Piedra aplasta tijera')
elif turnoPs5 == 2 and turnoJugador == 1:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 3 and turnoJugador == 2:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Tijera corta papel')
else:
    print('EMPATE')
#tercera jugada
turnoJugador = int(input('Que eliges?: '))
turnoPs5 = r.randint(1,3) #número aleatorio entre 1 y 3
print('PS5 eligió:', turnoPs5)
#resuelvo el cachipún con las condiciones posibles
#primero cuando gana jugador
if turnoPs5 == 1 and turnoJugador == 2:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 2 and turnoJugador == 3:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Tijera corta papel')
elif turnoPs5 == 3 and turnoJugador == 1:
    jugadorGana = jugadorGana + 1
    print('GANASTE')
    print('Piedra aplasta tijera')
#luego cuando pierde el jugador
elif turnoPs5 == 1 and turnoJugador == 3:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Piedra aplasta tijera')
elif turnoPs5 == 2 and turnoJugador == 1:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Papel envuelve piedra')
elif turnoPs5 == 3 and turnoJugador == 2:
    ps5Gana = ps5Gana + 1
    print('PERDISTE')
    print('Tijera corta papel')
else:
    print('EMPATE')
#entrego ganador
print('*.*'*15)
print('\tCACHIPÚN - Resultado Final')
print('*.*'*15)
if jugadorGana > ps5Gana:
    print(f'Ganaste {jugadorGana} a {ps5Gana}.')
elif jugadorGana < ps5Gana:
    print(f'Perdiste {jugadorGana} a {ps5Gana}.')
else:
    print(f'Empate {jugadorGana} a {ps5Gana}.')