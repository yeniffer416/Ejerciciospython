lista=[0,1,-3,4,-6,-10]
print('Esta es la lista que se pasara a positivo',lista)
lista=[(x>0)*x for x in lista]
print('Este es el resultado',lista)