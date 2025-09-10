from random import randint

print("--- PALPITES PARA A MEGA SENA ---\n")

quantidade_sorteios = int(input("Quantos jogos para ser sorteado? "))

lista_numeros_temporarios = []
lista_sorteio = []

contador_sorteio = 1
while contador_sorteio <= quantidade_sorteios:
    contador_numeros = 0
    while True:
        numero_aleatorio = randint(1, 60)
        if numero_aleatorio not in lista_numeros_temporarios:
            lista_numeros_temporarios.append(numero_aleatorio)
            contador_numeros += 1
        if contador_numeros >= 6:
            break
    lista_numeros_temporarios.sort()
    lista_sorteio.append(lista_numeros_temporarios[:])
    lista_numeros_temporarios.clear()
    contador_sorteio += 1

print("\n--- Sorteios ---\n")

for indice, jogo in enumerate(lista_sorteio):
    print(f"{indice + 1}º Sorteio: {jogo}")

#Usando o Sample.
from random import sample

print("\n--- PALPITES PARA A MEGA SENA ---\n")

quantidade_sorteios = int(input("Quantos jogos para ser sorteado? "))

print("\n--- Sorteios ---\n")

for i in range(quantidade_sorteios):
    jogo = sorted(sample(range(1, 61), 6))
    print(f"{i + 1}º Sorteio: {jogo}")
