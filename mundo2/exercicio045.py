from random import randint
from time import sleep

opcao_computador = randint(1, 3)
if opcao_computador == 1:
    jogada_computador = "PEDRA"
elif opcao_computador == 2:
    jogada_computador = "PAPEL"
elif opcao_computador == 3:
    jogada_computador = "TESOURA"

print("--- JOGO: PEDRA, PAPEL E TESOURA ---\n")

print("[ 1 ] - PEDRA")
print("[ 2 ] - PAPEL")
print("[ 3 ] - TESOURA\n")

opcao_usuario = int(input("Digite a sua opção (1, 2 ou 3): "))
print("\nPedra...", end=' ')
sleep(0.85)
print("Papel...", end=' ')
sleep(0.85)
print("E Tesoura\n")
sleep(0.85)

if opcao_usuario == 1:
    jogada_usuario = "PEDRA"
    if opcao_computador == 2:
        ganhador = "Computador"
    elif opcao_computador == 3:
        ganhador = "Jogador(a)"

elif opcao_usuario == 2:
    jogada_usuario = "PAPEL"
    if opcao_computador == 1:
        ganhador = "Jogador"
    elif opcao_computador == 3:
        ganhador = "Computador"

elif opcao_usuario == 3:
    jogada_usuario = "TESOURA"
    if opcao_computador == 1:
        ganhador = "Computador"
    elif opcao_computador == 2:
        ganhador = "Jogador"

print("--- \"Maõs\" --- \n")
print(f"Opção do Jogador: {jogada_usuario} ")
print(f"Opção do Computador: {jogada_computador} ")

print("\n--- Ganhador ---\n")
if opcao_usuario != opcao_computador:
    print(f"{ganhador} ganhou!")
    if ganhador == "Computador":
        print("Mais sorte na próxima vez!")
    else:
        print("Parabéns pela vitória!")

elif opcao_usuario == opcao_computador:
    print("Houve um empate!")
