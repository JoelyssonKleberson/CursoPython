frase_usuario = str(input("Digite uma frase: ")).strip().upper().split()
frase_usuario = ''.join(frase_usuario)
inverso_frase_usuario = frase_usuario[::-1]

print(f"\nO inverso da frase \'{frase_usuario}\' é {inverso_frase_usuario}")
if frase_usuario == inverso_frase_usuario:
    print(f"A frase \'{frase_usuario}\' É UM PALÍNDROMO!")
else:
    print(f"A frase \'{frase_usuario}\' NÃO É UM PALÍNDROMO!")
