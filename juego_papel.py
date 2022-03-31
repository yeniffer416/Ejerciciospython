#import random
#random.randrange(0, 3)

print("Juega piedra, papel o tijeras")
print("   ")
jugador1 = input("jugador 1 cual elijes: ")
print("   ")
jugador2 = input("jugador 2 cual elijes: ")
if jugador1 == jugador2:
    msg = 'Empate'
    winner = 0
elif jugador1 == 'piedra' and jugador2 == 'tijeras':
    msg = 'La piedra aplasta la tijeras'
    winner = 1
elif jugador1 == 'tijeras' and jugador2 == 'piedra':
    msg = 'La piedra aplasta la tijeras'
    winner = 2
elif jugador1 == 'tijeras' and jugador2 == 'papel':
    msg = 'La tijeras corta el papel'
    winner = 1
elif jugador1 == 'papel' and jugador2 == 'tijeras':
    msg = 'La tijeras corta el papel'
    winner = 2
elif jugador1 == 'papel' and jugador2 == 'piedra':
    msg = 'El papel envuelve la piedra'
    winner = 1
elif jugador1 == 'piedra' and jugador2 == 'papel':
    msg = 'El papel envuelve la piedra'
    winner = 2

if winner == 0:
    msg = 'Empate'
else:
    msg = f'Gana persona{winner}: {msg}'
print(msg)
