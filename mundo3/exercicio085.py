lista_numeros = [[], []]
for numeros in range(1, 8):
    numero_usuario = int(input(f"Digite o {numeros}º número: "))
    if numero_usuario % 2 == 0:
        lista_numeros[0].append(numero_usuario)
    else:
        lista_numeros[1].append(numero_usuario)

lista_numeros[0].sort()
lista_numeros[1].sort()

print(f"\nValore(s) Pare(s) Digitado(s): {lista_numeros[0]}")
print(f"Valore(s) Ímpare(s) Digitado(s): {lista_numeros[1]}")
