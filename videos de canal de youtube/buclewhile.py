'''bucle wwhile, raiz cuadrada'''

import math
numero=int(input("Digite un numero: "))
while numero<0:
    print("Error-> debe ser un numero positivo")
    numero=int(input("digite un numero "))

print((f"\n su raiz cuadrada es: {(math.sqrt(numero)):.2f}"))