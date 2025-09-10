while True:
    numero_usuario = int(input("Digite um número: "))
    if numero_usuario < 0:
        print("\nPrograma encerrado!")
        break
    print(f"\n--- TABUADA DO {numero_usuario} ---\n")
    contador = 1
    
    
    for tabuada in range(1, 11):
        multiplicacao = numero_usuario * tabuada
        print(f"{numero_usuario} x {tabuada} = {multiplicacao}")
    print("\n--- FIM DA TABUADA ---\n")
