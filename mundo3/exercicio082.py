lista_numeros = []
lista_pares = []
lista_impares = []

continuar = "S"
while continuar == "S":
    numero_usuario = int(input("Digite um número: "))
    lista_numeros.append(numero_usuario)

    if numero_usuario % 2 == 0:
        lista_pares.append(numero_usuario)
    elif numero_usuario % 2 == 1:
        lista_impares.append(numero_usuario)

    continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

print(f"\nNúmeros Digitados: {lista_numeros}")
print(f"Números Pares: {lista_pares}")
print(f"Números Ímpares: {lista_impares}")
