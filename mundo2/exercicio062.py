print("--- Progressão Aritmética ---\n")

primeiro_termo = int(input("Digite o Primeiro Termo da P.A.: "))
razao_usuario = int(input("Digites a Razão da P.A.: "))
numero_atual = primeiro_termo
termos_usuario = 10
print(f"\n{primeiro_termo} -> ", end='')

contador = 1
while contador < termos_usuario:
    numero_atual += razao_usuario
    print(f"{numero_atual} -> ", end='')
    contador += 1

    if contador == termos_usuario:
        print("PAUSA")
        opcao_usuario = str(input("\nDeseja continuar a sequência da P.A. (S/N)? ")).strip().upper()[0]
        if opcao_usuario == "S":
            termos_usuario = int(input("Digite x termos para a P.A.: "))
            contador = 0
            print()

print("\n--- Fim da P.A. ---")
