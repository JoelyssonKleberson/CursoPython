import moeda

preco = float(input("Digite o preço: R$"))

print(f"\nAumento de 10% sobre \'R${preco}\': R${moeda.aumento_numero(preco, 10)}")
print(f"Redução de 10% sobre \'R${preco}\': R${moeda.diminuir_numero(preco, 10)}")
print(f"Dobro de \'R${preco}\': R${moeda.dobro_numero(preco)}")
print(f"Metade de \'R${preco}\': R${moeda.metade_numero(preco)}")
