from biblioteca.interface_menu import *
from biblioteca.arquivos import *

arquivo = "mundo3exercicio115.txt"
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu()
    
    if resposta == "A":
        ler_arquivos(arquivo)

    elif resposta == "B":
        print("-"*30)
        print("--- Cadastrar Nova Pessoa ---".center(30))
        print("-"*30)
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arquivo, nome, idade)

    elif resposta == "C":
        print("\nSaindo do sistema... Até logo!")
        break
