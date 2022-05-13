import math
lista=[]

for x in range(20):
    valor=int(input('escriba un numero:  '))
    lista.append(valor)
    if lista [x]<0:
        lista [x]=int(input('escriba un numero positivo porfavor:  '))
print(lista)  