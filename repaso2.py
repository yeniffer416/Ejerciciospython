ruta='//1.1.1.1/eoi/python'

ruta=ruta[2:]
barra=ruta.index('/')

equipo=ruta[:barra]
ruta=ruta[barra:]
print(f'equipo={equipo};ruta={ruta}')