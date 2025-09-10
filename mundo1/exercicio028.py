from random import randint

numero_computador = randint(0, 5)
print("Tente advinhar qual número inteiro estou pensando!")
numero_jogador = int(input("Digite um número entre 0 e 5: "))

if numero_jogador == numero_computador:
    print("\nParabéns! Você acertou o número!")
else:
    print(f"\nErrado! Meu número é o {numero_computador}")
