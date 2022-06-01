# este es un ejemplo de funciones 
#crear ejemplo
def ejemplo(a,b):
    c=a+b
    print(f'este es el resultado de la suma: {c}')
    d=a*b
    print(f'este es el resultado de la multiplicacion: {d}')
    e=a/b
    print(f'este es el resultado de la division: {e}')
    f=a-b
    print(f'este es el resultado de la resta: {f}')
    pass #palabra reservada para cuando el campo este vacion y no de error

#colocar la variable en la funcion principal
def ejemplo1(a,b):
    c=a+b
    return c

#promaga principal
a=int(input('digite un numero '))
b=int(input('digite un numero '))


#llamar la funcion

ejemplo(a,b)
#se puede imprimir la funcion en un print
print(f'el resultado de la suma es:{ejemplo1(a,b)}')