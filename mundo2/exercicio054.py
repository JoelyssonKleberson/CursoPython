from datetime import date
maior_idade = menor_idade = 0
ano_atual = date.today().year

for nascimento in range(1, 8):
    ano_nascimento = int(input(f"Ano de nascimento da {nascimento}ª pessoa: "))

    idade = ano_atual - ano_nascimento
    if idade < 18:
        menor_idade += 1
    else:
        maior_idade += 1

print(f"\nMaiores de Idade: {maior_idade} pessoa(s)")
print(f"Menores de Idade: {menor_idade} pessoa(s)")
