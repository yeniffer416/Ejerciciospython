print("calcular los multiplos digitados por el usuario")
valorn=int(input("digite un numero para sacar el multiplo: "))
valorm=int(input("digite un numero para la cantidad a sacar del multiplo: "))

def generar_multiplos(valorn,valorm):
    return [valorn * i for i in range(1,valorm + 1)]
print(generar_multiplos(valorn,valorm))
