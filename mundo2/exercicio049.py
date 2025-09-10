numero_usuario = int(input("Digite um número: "))

print(f"--- Tabuada do {numero_usuario} ---\n")

for multiplicando in range(1, 11):
    multiplicacao = numero_usuario * multiplicando
    print(f"{numero_usuario} x {multiplicando:2} = {multiplicacao}")
