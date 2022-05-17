meses_produccion_2021= {'enero' :823879,'febrero':2682712,'marzo':817291,'abril':87281231,'mayo':728739,'junio':7286218,'julio':8287171,'agosto':67326,'septiembre':72837,'octubre':2314,'noviembre':612762,'diciembre':8263}

total=0              
valores= meses_produccion_2021.values()
elemetos = meses_produccion_2021.items()

min_key=  min(meses_produccion_2021, key=meses_produccion_2021.get)
Keymax = max(meses_produccion_2021, key=meses_produccion_2021.get)

for key, value in   meses_produccion_2021.items():
    total+=meses_produccion_2021[key]
    promedio=total/12

print('el mes con la mayor produccion es:',Keymax,'y su valor es',meses_produccion_2021[Keymax])
print('el mes con la menor produccion es:','y su valor es',min_key,meses_produccion_2021[min_key])
print('el promedio de produccion es: ',promedio)

for key in meses_produccion_2021.keys():
    if meses_produccion_2021[key]>=promedio:
        print('los meses por encima del promedio son: ',key)
        
for key in meses_produccion_2021.keys():
    if meses_produccion_2021[key]<=promedio:
        print('los meses por debajo del promedio son: ',key)
