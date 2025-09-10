def menu():
    print("-"*30)
    print("--- Menu Principal ---".center(30))
    print("-"*30)
    print("\nA - Ver Pessoas Cadastradas;")
    print("B - Cadastrar Novas Pessoas;")
    print("C - Sair do Sistema;\n")

    lista_opcoes = ["A", "B", "C"]
    opcao_menu = ""
    while opcao_menu not in lista_opcoes:
        opcao_menu = str(input("Digite uma Opção do Menu (A, B ou C): ")).strip().upper()
        if opcao_menu not in lista_opcoes:
            print("\033[31m Opção Inválida! \033[0m")

    return opcao_menu
