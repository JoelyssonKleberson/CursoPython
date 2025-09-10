soma_pares = 0
for numeros in range(6):
    numero_usuario = int(input("Digite um número inteiro: "))
    if numero_usuario % 2 == 0:
        soma_pares += numero_usuario

print(f"\nA soma dos números pares digitados é \'{soma_pares}\'")
