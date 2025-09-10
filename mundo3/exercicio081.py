lista_numeros = []
continuar = "S"
while continuar == "S":
    numero_usuario = int(input("Digite um número: "))
    lista_numeros.append(numero_usuario)

    continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

print(f"\nNúmeros digitados: {len(lista_numeros)} número(s)")
print(f"Valores digitados (Decrescente): {sorted(lista_numeros, reverse = True)}")

if 5 in lista_numeros:
    print("O número \'5\' está na Lista!")
elif 5 not in lista_numeros:
    print("O número \'5\' NÃO está na Lista!")
