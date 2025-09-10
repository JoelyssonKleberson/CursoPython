cadastro_pessoa = {}
lista_mulheresCadastradas = []
lista_cadastrados = []
lista_idades = []

print("--- Cadastro de Pessoas ---")
continuar = "S"
while continuar == "S":
    cadastro_pessoa['Nome'] = str(input("\nNome: ")).strip().capitalize()

    cadastro_pessoa['Sexo'] = ""
    while cadastro_pessoa['Sexo'] not in ["M", "F"]:
        cadastro_pessoa['Sexo'] = str(input("Sexo (M/F): ")).strip().upper()[0]
        if cadastro_pessoa["Sexo"] not in ["M", "F"]:
            print("Sexo Inválido!")
    if cadastro_pessoa['Sexo'] == "F":
        lista_mulheresCadastradas.append(cadastro_pessoa['Nome'])

    cadastro_pessoa['Idade'] = int(input("Idade: "))
    lista_idades.append(cadastro_pessoa['Idade'])

    lista_cadastrados.append(cadastro_pessoa.copy())
    cadastro_pessoa.clear()

    continuar = ""
    while ((continuar != "S") and (continuar != "N")):
        continuar = str(input("Deseja continuar (S/N): ")).strip().upper()[0]
        if ((continuar != "S") and (continuar != "N")):
            print("Opção Inválida!")

print("\n--- Fim do(s) Cadastro(s) ---\n")
print(f"Pessoa(s) Cadastrada(s): {len(lista_cadastrados)} pessoa(s)")

media_idades = sum(lista_idades) / len(lista_idades)
print(f"Média da(s) Idade(s): {media_idades:.2f} ano(s)")

print("Mulher(es) Cadastrada(s): ", end='')
if not lista_mulheresCadastradas:
    print("Nenhuma mulher Cadastrada!")
elif len(lista_mulheresCadastradas) == 1:
    print(f"{lista_mulheresCadastradas[0]}")
else:
    for mulher in lista_mulheresCadastradas:
        if mulher == lista_mulheresCadastradas[-1]:
            print(f"{mulher}")
        else:
            print(f"{mulher} | ", end='')

print("Lista de Pessoas que estão Acima da Média:\n")
for pessoa in lista_cadastrados:
    if pessoa['Idade'] >= media_idades:
        for dados, dados_usuario in pessoa.items():
            print(f"{dados}: {dados_usuario}; ", end='')
        print()
