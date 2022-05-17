lista1=[]
lista2=[]
#valor=int(input('escriba un numero:  '))
for x in range(2):
    valor=int(input('escriba un numero:  '))
    
    if valor%2==0:
        lista1.append(valor)
    else:
        lista2.append(valor)
 
print('lista 1',lista1)
print(lista2)