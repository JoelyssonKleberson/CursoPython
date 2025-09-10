print("--- Condição de Parada \'999\' ---\n")

lista_numeros = []
numeros_digitados = 0
numero_usuario = None
while numero_usuario is None or numero_usuario != 999:
    numero_usuario = int(input("Digite um valor: "))
    if numero_usuario == 999:
        continue
    else:
        lista_numeros.append(numero_usuario)
        numeros_digitados += 1

print(f"\nNúmeros digitados: {numeros_digitados} número(s)")
print(f"Soma dos números digitados: {sum(lista_numeros)}")
