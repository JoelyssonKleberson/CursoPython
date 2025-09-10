from random import randint

tupla_numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Números Sorteados: ",end='')

contador = 1
for numeros in tupla_numeros:
    if contador == 5:
        print(f"{numeros}")
    else:
        print(f"{numeros} - ", end='')

    contador += 1

print(f"Maior Valor Sorteado: {max(tupla_numeros)}")
print(f"Menor Valor Sorteado: {min(tupla_numeros)}")
