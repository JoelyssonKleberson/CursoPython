print(f"--- Sequência de Fibonacci ---\n")

termos_usuario = int(input("Digite x termos da Sequência: "))
primeiro_termo = 0
segundo_termo = 1
contador = 1

print(f"\n{primeiro_termo} -> {segundo_termo} -> ", end='')
while contador <= termos_usuario - 2:
    terceiro_termo = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo 
    contador += 1

    print(f"{terceiro_termo} -> ", end='')

print("Fim!")
