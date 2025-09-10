print("--- Fatorial ---\n")

numero_usuario = int(input("Digite um número: "))
fatorial = 1

print(f"{numero_usuario}! = ", end='')

while numero_usuario > 0:
    if numero_usuario > 1:
        print(f"{numero_usuario} x ", end='')
    else:
        print(f"{numero_usuario} = ", end='')
    fatorial *= numero_usuario
    numero_usuario -= 1

print(f"{fatorial}")
