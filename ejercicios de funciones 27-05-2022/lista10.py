def listas (lista):
    StrA='' 
    for x in lista:
        print(f'esta es la lista {x}')
        StrA = ''.join(lista)
        orden=lista.sort()
        print(f'esta es la lista ordenada:{orden}')
        print("1" in lista)
        
    print(f'esta es lista convertida en cadena:{StrA}')
        
#programa princpial
lista=[]
for x in range(3):
    valor=str(input('escriba un numero:  '))
    lista.append(valor)
    
print(lista)