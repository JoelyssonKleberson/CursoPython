from random import randint

def sorteio_numeros(lista):
    for _ in range(5):
        lista.append(randint(1, 10))
    print(f"Valores Sorteados: {lista_numeros}")

lista_numeros = []
sorteio_numeros(lista_numeros)

def soma_pares(lista_numeros, numeros_pares):
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros_pares += numero
    print(f"Soma dos Pares: {numeros_pares}")

numeros_pares = 0
soma_pares(lista_numeros, numeros_pares)
