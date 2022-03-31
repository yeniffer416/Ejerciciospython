puede_volar=str(input("puede volar "))
es_humano=str(input("¿es humano? "))
tiene_mascara=str(input("¿Tiene mascara "))


if puede_volar=="si":
    if es_humano=="si":
        if tiene_mascara=="si":
            print('Ironman')
        else:
            print('Captain Marvel')
    else:
        if tiene_mascara=="si":
            print('Ronan Accuser')
        else:
            print('Vision')
else:
    if es_humano=="si":
        if tiene_mascara:
            print('Spiderman')
        else:
            print('Hulk')
    else:
        if tiene_mascara=="si":
            print('Black Bolt')
        else:
            print('Thanos')
