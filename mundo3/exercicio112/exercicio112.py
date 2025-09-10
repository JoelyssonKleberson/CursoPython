from utilidadesCeV import moeda
from utilidadesCeV import dados

preco = dados.ler_valor("Digite um valor: R$")
moeda.resumo(preco, 35, 22)
