primeiro_numero = int(input("Digite o Primeiro Valor: "))
segundo_numero = int(input("Digite o Segundo Valor: "))

if primeiro_numero > segundo_numero:
    print(f"O Primeiro Valor ({primeiro_numero}) é Maior!")
elif segundo_numero > primeiro_numero:
    print(f"O Segundo Valor ({segundo_numero}) é Maior!")
elif primeiro_numero == segundo_numero:
    print("Os dois valores são Iguais!")