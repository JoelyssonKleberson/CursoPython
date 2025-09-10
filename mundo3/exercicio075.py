primeiro_numero = int(input("Digite o Primeiro número: "))
segundo_numero = int(input("Digite o Segundo número: "))
terceiro_numero = int(input("Digite o Terceiro número: "))
quarto_numero = int(input("Digite o Quarto número: "))

tupla_numeros = (primeiro_numero, segundo_numero, terceiro_numero, quarto_numero)
quantidade_9 = tupla_numeros.count(9)
numeros_pares = 0

for numeros in tupla_numeros:
    if numeros % 2 == 0:
        numeros_pares += 1

print(f"\nValores digitados: {tupla_numeros}")
print(f"\'9\' Apareceu: {quantidade_9} vez(es)")

if 3 in tupla_numeros:
    numero_3 = tupla_numeros.index(3)
    print(f"Posição do Número \'3\': {numero_3 + 1}ª posição")
else:
    print(f"O número \'3\' não apareceu em nenhuma posição!")

print(f"Números pares: {numeros_pares} número(s)")
