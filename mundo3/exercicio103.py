def jogadores_campeonato():
    nome = str(input("Nome do Jogador: ")).strip().capitalize()
    gols = str(input("Número de Gol(s): "))

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome != "":
        print(f"\nJogador: {nome} - Gol(s): {gols}")
    else:
        print(f"\nJogador: \'Desconhecido\' - Gol(s): {gols}")
    
jogadores_campeonato()
