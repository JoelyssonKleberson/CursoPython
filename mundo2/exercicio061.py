print("--- 10 Termos de uma P.A ---\n")

primeiro_termo_usuario = int(input("Digite o primeiro Termo da P.A: "))
razao_usuario = int(input("Digite a razão da P.A: "))
contador = 1
numero_atual = primeiro_termo_usuario
print(f"\n{primeiro_termo_usuario} -> ", end='')

while contador < 10:
    numero_atual += razao_usuario
    print(f"{numero_atual} -> ", end='')
    contador += 1

print("Fim!")
