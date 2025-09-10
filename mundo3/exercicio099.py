def maior_valor(*numeros):
    maior_numero = 0
    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero

    print(f"Maior número: {maior_numero}")
maior_valor(9, 7, 5, 8, 1)
maior_valor(2, 7, 0)
maior_valor(1, 2)
maior_valor(7)
maior_valor()