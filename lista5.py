import math
frase=input('digite la frase: ')
cuentafrase=frase.split()
cuentafrase=list(map(str.upper,cuentafrase))
print(cuentafrase)
sinduplicado=set(cuentafrase)
print(sinduplicado)
