print("--- Lista de Números ---")

lista_numeros = []
continuar = ""
while continuar != "N":
    numero_usuario = float(input("\nDigite um número: "))
    if numero_usuario not in lista_numeros:
        lista_numeros.append(numero_usuario)
        print("Valor adicionado!")
    elif numero_usuario in lista_numeros:
        print("Este número já foi adicionado!")

    continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

print(f"\nNúmeros digitados em ordem Crescente: {sorted(lista_numeros)}")
