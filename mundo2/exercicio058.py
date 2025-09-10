from random import randint
numero_computador = randint(0, 10)

print("--- Jogo de Adivinhação ---")
print("--- ADIVINNHE UM NÚMERO ENTRE 0 e 10 ---")

tentativas = 0
numero_usuario = ""
while numero_usuario != numero_computador:
    numero_usuario = int(input("\nDigite um número inteiro: "))

    if numero_usuario < numero_computador:
        print(f"MAIOR que \'{numero_usuario}\'!")
    elif numero_usuario > numero_computador:
        print(f"MENOR que \'{numero_usuario}\'!")

    tentativas += 1

print(f"Parabéns, você acertou em {tentativas} tentativa(s)!")
