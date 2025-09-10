lista_principal_pessoas = []
dados_temporarios = []

maior_peso = 0
menor_peso = None

continuar = "S"
while continuar == "S":
    dados_temporarios.append(str(input("Nome: ")))
    dados_temporarios.append(float(input("Peso: ").replace(",", ".")))

    if dados_temporarios[1] > maior_peso:
        maior_peso = dados_temporarios[1]
    if menor_peso is None or dados_temporarios[1] < menor_peso:
        menor_peso = dados_temporarios[1]

    lista_principal_pessoas.append(dados_temporarios[:])
    dados_temporarios.clear()
    
    continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

print(f"\nPessoas Cadastradas: {len(lista_principal_pessoas)} pessoa(s)")

print(f"Maior peso: {maior_peso} kg. Nome(s): ", end='')
for pessoa in lista_principal_pessoas:
    if pessoa[1] == maior_peso:
        print(f"\'{pessoa[0]}\' ", end='')

print(f"\nMenor peso: {menor_peso} kg. Nome(s): ", end='')
for pessoa in lista_principal_pessoas:
    if pessoa[1] == menor_peso:
        print(f"\'{pessoa[0]}\' ", end='')
