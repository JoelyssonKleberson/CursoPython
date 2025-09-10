def aumento_numero(preco = 0, taxa = 0, formatado = False):
    '''
    >>> Função de Cálculo de aumento, redução, dobro e metade do valor de uma moeda.
        _ Parâmetro 'preço': valor da moeda dita pelo usuário;
        _ Parâmetro 'taxa': taxa fixa de 10% e 5%;
        _ Parâmetro 'formatado': se a formatação do preço aparecerá com vírgula, R$ e com duas casas decimais;
    '''
    novo_preco = preco + (preco * taxa/100)
    if formatado is False:
        return novo_preco
    else:
        return moeda(novo_preco)

def diminuir_numero(preco = 0, taxa = 0, formatado = False):
    novo_preco = preco * (1 - taxa/100)
    if formatado is False:
        return novo_preco
    else:
        return moeda(novo_preco)

def dobro_numero(preco = 0, formatado = False):
    novo_preco = preco * 2
    if formatado is False:
        return novo_preco
    else:
        return moeda(novo_preco)
def metade_numero(preco = 0, formatado = False):
    novo_preco = preco / 2
    if formatado is False:
        return novo_preco
    else:
        return moeda(novo_preco)

def moeda(preco = 0, valor_moeda = "R$"):
    return (f"{valor_moeda}{preco:.2f}"). replace(".", ",")

def resumo(preco = 0, taxaAumento = 10, taxaReducao = 5):
    print("\n--- Resumo dos Valores ---".center(30))
    print()
    print("-"*30)
    print(f"Preço: {moeda(preco)}")
    print("-"*30)
    print(f"Aumento de \'10%\': \t{aumento_numero(preco, taxaAumento, True)} ")
    print(f"Redução de \'5%\': \t{diminuir_numero(preco, taxaReducao, True)} ")
    print(f"Dobro de \'{moeda(preco)}\': \t{dobro_numero(preco, True)} ")
    print(f"Metade de \'{moeda(preco)}\': \t{metade_numero(preco, True)} ")
    print("-"*30)
