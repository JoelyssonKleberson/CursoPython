def aumento_numero(preco, taxa):
    novo_preco = preco + (preco * taxa/100)
    return novo_preco

def diminuir_numero(preco, taxa):
    novo_preco = preco * (1 - taxa/100)
    return novo_preco

def dobro_numero(preco):
    novo_preco = preco * 2
    return novo_preco

def metade_numero(preco):
    novo_preco = preco / 2
    return novo_preco
