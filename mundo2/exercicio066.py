print("--- Condição de Parada \'999\' ---\n")

lista_numeros = []
while True:
    numero_usuario = int(input("Digite um número: "))
    if numero_usuario == 999:
        break

    lista_numeros.append(numero_usuario)

print(f"\nNúmeros digitados: {len(lista_numeros)} número(s)")
print(f"Soma dos números digitados: {sum(lista_numeros)}")
