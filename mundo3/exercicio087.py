matriz = [
    [0,0,0], 
    [0,0,0], 
    [0,0,0]
            ]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um número [{linha}, {coluna}]: "))
print()

soma_pares = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()

print(f"\nSoma dos números \'Pares\': {soma_pares}")

soma_coluna = 0
for linha in range(3):
    soma_coluna += matriz[linha][2]
print(f"Soma dos números da 3ª \'Coluna\': {soma_coluna}")

maior_linha = None

for coluna in range(3):
    if maior_linha is None or matriz[1][coluna] > maior_linha:
        maior_linha = matriz[1][coluna]
print(f"Maior número da 2ª \'Linha\': {maior_linha}")
