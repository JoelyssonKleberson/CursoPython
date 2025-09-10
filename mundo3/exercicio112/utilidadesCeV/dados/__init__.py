def ler_valor(mensagem_usuario):
    validacao = False
    while not validacao:
        opcao_usuario = str(input(mensagem_usuario)).replace(",", ".").strip()
        if opcao_usuario.isalpha() or opcao_usuario == "":
            print('\033[0;31m'"Preço inválido!", '\033[m')
        else:
            validacao = True
    
    return float(opcao_usuario)
