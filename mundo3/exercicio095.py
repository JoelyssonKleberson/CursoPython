lista_jogadores = []
dados_jogador = {}

print("--- Cadastro de Jogadores ---")
continuar = "S"
while continuar == "S":
    dados_jogador['Nome'] = str(input("\nNome do Jogador: ")).strip().capitalize()
    
    quantidade_jogos = int(input(f"Quantas partidas \'{dados_jogador['Nome']}\' jogou? "))
    lista_gols = []
    for partidas in range(quantidade_jogos):
        gols_partida = int(input(f"Quantos gols na {partidas + 1}º partida? "))
        lista_gols.append(gols_partida)
    dados_jogador['Gols'] = lista_gols
    dados_jogador['Total de Gols'] = sum(lista_gols)

    lista_jogadores.append(dados_jogador.copy())
    dados_jogador.clear()

    continuar = ""
    while continuar not in ["S", "N"]:
        continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]
        if continuar not in ["S", "N"]:
            print("Opção inválida!")

print("\n--- Fim do(s) Cadastro(s) ---\n")

print("--- Tabela do(s) Jogadore(s) ---\n")
print("-"*50)
print(f"{"No.":<5}{"Nome:":>5}{"Gols:":>15}{"Total de Gols":>20}")
print("-"*50)

for chave, valor in enumerate(lista_jogadores, start=1):
    print(f"{chave:<5}", end='')
    for dado in valor.values():
        print(f"{str(dado):<15}", end='')
    print()
print("-"*50)

ver_jogador = str(input("\nDeseja ver os Dados Individuais (Sim ou Não)? ")).strip().upper()[0]
if ver_jogador == "S":
    while ver_jogador == "S":
        ver_dados_jogador = int(input("Digite a Numeração do Jogador: "))
        if ver_dados_jogador > len(lista_jogadores) or ver_dados_jogador <= 0:
            print("Número inválido!")
        elif ver_dados_jogador <= len(lista_jogadores):
            print("\n--- Dados Individuais ---\n")
            print("-"*33)
            print(f"{"Jogador:":<10}{"Gols:"}")
            print("-"*33)
            jogador = lista_jogadores[ver_dados_jogador - 1]
            print(f"{jogador['Nome']:<10}{jogador['Gols']}")
            print("-"*33)

            ver_jogador = str(input("\nDeseja ver as Mais Dados Individuais (Sim ou Não)? ")).strip().upper()[0]

print("\n--- Fim do Processo ---")