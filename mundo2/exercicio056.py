lista_idades = []
mulher_menor = 0
idade_velho = 0
nome_velho = ""

for pessoas in range(1, 5):
    if pessoas == 1:
        print(f"--- {pessoas}ª Pessoa ---\n")
    else:
        print(f"\n--- {pessoas}ª Pessoa ---\n")

    nome = str(input("Digite o seu nome: ")).capitalize()
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite o seu sexo (M/F): ")).strip().upper()

    lista_idades.append(idade)
    media_idades = (sum(lista_idades) / len(lista_idades))

    if sexo == "M":
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome

    if ((sexo == "F") and (idade < 20)):
        mulher_menor += 1

print(f"\nMédia das idades: {media_idades:.2f} anos")
print(f"Homem mais velho: {nome_velho}, {idade_velho} anos")
print(f"Mulheres menor que 20 anos: {mulher_menor} mulher(es)")
