print("--- 10 Termos de uma P.A ---\n")

primeiro_termo_usuario = int(input("Digite o Primeiro Termo da P.A: "))
razao_usuario = int(input("Digite a razão da P.A: "))
n_esimo_termo = primeiro_termo_usuario + (10 - 1) * razao_usuario
print()

for pa in range(primeiro_termo_usuario, n_esimo_termo + razao_usuario, razao_usuario):
    print(f"{pa} ->", end=' ')

print("Fim!")
