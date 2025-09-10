lista_numeros = []
continuar = "S"
while continuar == "S":
    numero_usuario = float(input("Digite um número: "))
    lista_numeros.append(numero_usuario)

    continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]
    print()

print(f"Números digitados: {len(lista_numeros)} número(s)")
print(f"Média: {sum(lista_numeros) / len(lista_numeros):.2f}")
print(f"Maior número: {max(lista_numeros)}")
print(f"Menor número: {min(lista_numeros)}")
 