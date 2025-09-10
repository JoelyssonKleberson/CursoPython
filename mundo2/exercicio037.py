numero_usuario = int(input("Digite um número inteiro: "))

print("\n --- Menu de Opções --- \n")
print(f"[ 1 ] - Converter \'{numero_usuario}\' para BINÁRIO")
print(f"[ 2 ] - Converter \'{numero_usuario}\' para OCTAL")
print(f"[ 3 ] - Converter \'{numero_usuario}\' para HEXADECIMAL\n")

opcao_usuario = str(input("Digite uma das opções (1, 2 ou 3): "))
if opcao_usuario == "1":
    binario = bin(numero_usuario)
    print(f"\n\'{numero_usuario}\' em Binário: {binario[2:]}(2)")

elif opcao_usuario == "2":
    octal = oct(numero_usuario)
    print(f"\n\'{numero_usuario}\' em Octal: {octal[2:]}(8)")

elif opcao_usuario == "3":
    hexadecimal = hex(numero_usuario)
    print(f"\n\'{numero_usuario}\' em Hexadecimal: {hexadecimal[2:]}(16)")

else:
    print("Opção inválida!")
