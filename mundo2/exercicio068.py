from random import randint
from time import sleep

numero_computador = randint(1, 20)
contador_vitorias = 0
print("--- JOGO: PAR OU ÍMPAR ---\n")

while True:
    numero_usuario = int(input("Digite um número: "))

    lista_opcoes = ["P", "I", "Í"]
    par_impar_usuario = ""
    while par_impar_usuario not in lista_opcoes:
        par_impar_usuario = str(input("Par ou Ímpar (P ou I)? ")).strip().upper()[0]

    soma_usuario_computador = numero_usuario + numero_computador
    if par_impar_usuario == "P":
        if soma_usuario_computador % 2 == 0:
            ganhador = "Jogador"
        else:
            ganhador = "Computador"
        
    elif par_impar_usuario in "IÍ":
        if soma_usuario_computador % 2 != 0:
            ganhador = "Jogador"
        else:
            ganhador = "Computador"

    print("\n--- Opções ---\n")

    if par_impar_usuario == "P":
        print("JOGADOR: Par...")
        sleep(0.5)
        print("COMPUTADOR: Ímpar...")
        sleep(0.5)
        print("JOGADOR E COMPUTADOR: 1, 2, 3 e já...\n")
    
    else:
        print("JOGADOR: Ímpar...")
        sleep(0.5)
        print("COMPUTADOR: Par...")
        sleep(0.5)
        print("JOGADOR E COMPUTADOR: 1, 2, 3 e já...")

    sleep(1)
    print("\n--- \'Mãos\' ---\n")
            
    print(f"JOGADOR: {numero_usuario}")
    print(f"COMPUTADOR: {numero_computador}")

    if soma_usuario_computador % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"
    print(f"{numero_usuario} + {numero_computador} = {soma_usuario_computador} ({resultado})")

    sleep(1)
    print("\n--- GANHADOR ---\n")
    if numero_usuario == numero_computador:
        print("Houve um Empate!")
    else:
        print(f"\'{ganhador}\' Venceu!")
    
    if ((ganhador == "Computador") and (numero_usuario != numero_computador)):
        print("Mais sorte na próxima vez!")
        break
    elif ((ganhador == "Jogador") and (numero_usuario != numero_computador)):
        print("Parabéns pela vitória!")
        contador_vitorias += 1

    print("\n--- TENTE MAIS UMA VEZ! ---\n")

print(f"\nVitórias Consecutivas: {contador_vitorias} vitória(s)")
