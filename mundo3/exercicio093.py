dados_jogador = {}
dados_jogador['nome'] = str(input("Nome: ")).strip().capitalize()

quantidade_jogos = int(input(f"Quantas partidas {dados_jogador['nome']} jogou? "))
lista_gols = []
for partidas in range(quantidade_jogos):
    gols_partida = int(input(f"Quantos gols na {partidas + 1}º partida? "))
    lista_gols.append(gols_partida)
dados_jogador['gols'] = lista_gols
dados_jogador['total de gols'] = sum(lista_gols)

print("\n--- Dados ---\n")
print(dados_jogador)
for dados, dados_usuario in dados_jogador.items():
    print(f"{dados}: {dados_usuario}")
print("\n--- Fim dos Dados ---\n")

print("--- Partida(s) ---\n")

print(f"Jogador: \'{dados_jogador['nome']}\' - Partidas: {quantidade_jogos} partida(s)")
for partidas in range(quantidade_jogos):
    print(f"{partidas + 1}º Partida: {dados_jogador['gols'][partidas]} gols")
print(f"Total de gols: {sum(lista_gols)} gol(s)")
