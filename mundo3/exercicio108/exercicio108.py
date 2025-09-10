import moeda

preco = float(input("Digite o preço: R$"))

print(f"\nAumento de 10% sobre \'{moeda.moeda(preco)}\': {moeda.moeda(moeda.aumento_numero(preco, 10))}")
print(f"Redução de 10% sobre \'{moeda.moeda(preco)}\': {moeda.moeda(moeda.diminuir_numero(preco, 10))}")
print(f"Dobro de \'{moeda.moeda(preco)}\': {moeda.moeda(moeda.dobro_numero(preco))}")
print(f"Metade de \'{moeda.moeda(preco)}\': {moeda.moeda(moeda.metade_numero(preco))}")
