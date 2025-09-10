numero_usuario = int(input("Digite um número: "))
total_dividido = 0

for numeros in range(1, numero_usuario + 1):
    if numero_usuario % numeros == 0:
        print('\033[33m', end=' ')
        total_dividido += 1
    
    else:
        print('\033[31m', end=' ')
    print(f"{numeros}", end=' ')

print()
print(f"\n\033[mO número \'{numero_usuario}\' foi dividido {total_dividido} vez(es)")
if total_dividido == 2:
    print(f"\'{numero_usuario}\' É PRIMO!")
else:
    print(f"\'{numero_usuario}\' NÃO É PRIMO!")
