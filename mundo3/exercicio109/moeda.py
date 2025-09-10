def aumento_numero(preco = 0, taxa = 0, formatado = False):
    '''
    >>> Função de Cálculo de aumento, redução, dobro e metade do valor de uma moeda.
        _ Parâmetro 'preço': valor da moeda dita pelo usuário;
        _ Parâmetro 'taxa': taxa fixa de 10%;
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