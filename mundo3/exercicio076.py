tupla_itens = ("Switch", 2400, "PS5", 3700, "Celular", 2800, "Notebook", 3000, "Fone", 150, "Mouse", 700, "PC", 9000)
print(f"{"--- Lista de Preços ---":^30}\n")

for posicao in range(0, len(tupla_itens)):
    if posicao % 2 == 0:
        print(f"{tupla_itens[posicao]:.<20}", end='')
    else:
        print(f"R${tupla_itens[posicao]:>1.2f}")
