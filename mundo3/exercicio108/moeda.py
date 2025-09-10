def aumento_numero(preco = 0, taxa = 0):
    novo_preco = preco + (preco * taxa/100)
    return novo_preco

def diminuir_numero(preco = 0, taxa = 0):
    novo_preco = preco * (1 - taxa/100)
    return novo_preco

def dobro_numero(preco = 0):
    novo_preco = preco * 2
    return novo_preco

def metade_numero(preco = 0):
    novo_preco = preco / 2
    return novo_preco

def moeda(preco = 0, valor_moeda = "R$"):
    return (f"{valor_moeda}{preco:.2f}"). replace(".", ",")