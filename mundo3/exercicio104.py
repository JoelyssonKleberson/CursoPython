def validacao_numero():
    while True:
        numero_usuario = str(input("Digite um número: "))
        if numero_usuario.isnumeric():
            break
        else:
            print("Erro! Digite outro número!")

    return numero_usuario

numero_validado = validacao_numero()
print(f"\nNúmero Digitado: {numero_validado}")
