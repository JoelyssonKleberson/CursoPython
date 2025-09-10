lista_numeros = []

for numeros in range(1, 6):
    numeros_usuario = float(input(f"Digite o {numeros}º número: ").strip())
    lista_numeros.append(numeros_usuario)

maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

maior_valor_indece = lista_numeros.index(maior_valor)
menor_valor_indece = lista_numeros.index(menor_valor)

print(f"\nValores digitados: {lista_numeros}")
print(f"Maior valor digitado: {maior_valor}, índice {maior_valor_indece + 1}")
print(f"Menor valor digitado: {menor_valor}, índice {menor_valor_indece + 1}")