import moeda

preco = float(input("Digite o preço: R$"))

print(f"\nAumento de 10% sobre \'{moeda.moeda(preco)}\': {moeda.aumento_numero(preco, 10, True)}") #Posso 'Não' colocar nada que por padrão vai ser 'False' (moeda.diminuir_numero(preco, 10)).
print(f"Redução de 10% sobre \'{moeda.moeda(preco)}\': {moeda.diminuir_numero(preco, 10, True)}") #Posso colocar 'False' (moeda.diminuir_numero(preco, 10, False)).
print(f"Dobro de \'{moeda.moeda(preco)}\': {moeda.dobro_numero(preco, True)}")
print(f"Metade de \'{moeda.moeda(preco)}\': {moeda.metade_numero(preco, True)}")
