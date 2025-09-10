def fatorial(numero):
    '''
    >>> Cálculo do fatorial de um número!
        _ Parâmetro 'numero': número do usuário;
        _ Parâmetro 'return': retorna a conta do fatorial para o usuário;
    '''
    fatorial_calculo = 1
    contador_numeros = numero
    for valor in range(numero, 0, -1):
        fatorial_calculo *= valor
        if contador_numeros == 1:
            print(f"{contador_numeros}", end=' ')
        else:
            print(f"{contador_numeros} x", end=' ')
        contador_numeros -= 1

    return fatorial_calculo
    
fatorial_resultado = fatorial(int(input("Fatorial de: ")))
print(f"= {fatorial_resultado}")

help(fatorial)