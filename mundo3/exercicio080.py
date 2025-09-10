lista_numeros = []
menor_numero = maior_numero = 0
for valores in range(1, 6):
    numero_usuario = int(input("Digite um número: "))

    if valores == 1 or numero_usuario > lista_numeros[-1]:
        lista_numeros.append(numero_usuario)
        print(f"Número \'{numero_usuario}\' adicionado ao final da lista!\n")
    else:
        posicao_numero_usuario = 0
        while posicao_numero_usuario < len(lista_numeros):
            if numero_usuario <= lista_numeros[posicao_numero_usuario]:
                lista_numeros.insert(posicao_numero_usuario, numero_usuario)
                print(f"Número \'{numero_usuario}\' adicionado na {posicao_numero_usuario + 1}ª posição!\n")
                break
            posicao_numero_usuario += 1

print(f"Valores digitados: {lista_numeros}")
