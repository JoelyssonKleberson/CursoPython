print("--- Menu de Opções ---\n")
primeiro_valor = int(input("Digite o 1º valor: "))
segundo_valor = int(input("Digite o 2º valor: "))

lista_opcoes = ["A", "B", "C", "D", "E"]
opcao_usuario = ""
while opcao_usuario != "E":
    print("\n--- Menu de Opções ---\n")

    print("[ A ] - Somar")
    print("[ B ] - Multiplicar")
    print("[ C ] - Maior Número ")
    print("[ D ] - Novos Números")
    print("[ E ] - Sair\n")

    opcao_usuario = str(input("Digite uma das opções (A, B, C, D ou E): ")).strip().upper()
    if opcao_usuario == "A":
        soma = primeiro_valor + segundo_valor
        print(f"{primeiro_valor} + {segundo_valor} = {soma}")
    
    elif opcao_usuario == "B":
        multiplicacao = primeiro_valor * segundo_valor
        print(f"{primeiro_valor} x {segundo_valor} = {multiplicacao}")

    elif opcao_usuario == "C":
        if primeiro_valor > segundo_valor:
            print(f"Maior: {primeiro_valor}")
        elif segundo_valor > primeiro_valor:
            print(f"Maior: {segundo_valor}\n")
        elif primeiro_valor == segundo_valor:
            print("Ambos são iguais!")
        
    elif opcao_usuario == "D":
        primeiro_valor = int(input("Digite o 1º valor: "))
        segundo_valor = int(input("Digite o 2º valor: "))

    elif opcao_usuario not in lista_opcoes:
        print("Opção Inválida!")

print("Fim do Programa!")
