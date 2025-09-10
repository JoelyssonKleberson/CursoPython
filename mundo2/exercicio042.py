primeiro_lado = float(input("Digite o Primeiro Segmento: "))
segundo_lado = float(input("Digite o Segundo Segmento: "))
terceiro_lado = float(input("Digite o Terceiro Segmento: "))

if ((primeiro_lado < (segundo_lado + terceiro_lado)) and (segundo_lado < (primeiro_lado + terceiro_lado)) and (terceiro_lado < (primeiro_lado + segundo_lado))):
    print("\nOs Segmentos acima PODEM FORMAR um triângulo", end=" ")
    if primeiro_lado == segundo_lado == terceiro_lado:
        print("EQUILÁTERO!")
    elif primeiro_lado != segundo_lado != terceiro_lado != primeiro_lado:
        print("ESCALENO!")
    else:
        print("ISÓCELES!")

else:
    print("\nOs Segmentos acima NÃO PODEM FORMAR um triângulo!")
