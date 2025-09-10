from random import randint
from operator import itemgetter

jogadas = {"Jogador 1": randint(1, 6),
           "Jogador 2": randint(1, 6),
           "Jogador 3": randint(1, 6),
           "Jogador 4": randint(1, 6)}

print("--- Valores Sorteados ---\n")

for jogador, dado in jogadas.items():
    print(f"*{jogador}: {dado}")

print("\n--- Ranking ---\n")

ranking = []
ranking = sorted(jogadas.items(), key = itemgetter(1), reverse = True)
for posicao, jogador in enumerate(ranking):
    print(f"{posicao + 1}º Lugar - {jogador[0]}: {jogador[1]}")
