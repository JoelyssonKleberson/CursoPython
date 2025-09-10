maiores_18 = mulheres_20 = homens_cadastrados = 0
contador_cadastro = 1
while True:
    if contador_cadastro == 1:
        print(f"--- Cadastro ---\n")
    else:
        print(f"\n--- Cadastro ---\n")
    idade = int(input("Digite a sua idade: "))

    lista_sexos = ["M", "F"]
    sexo = ""
    while sexo not in lista_sexos:
        sexo = str(input("Digite o seu sexo (M ou F): ")).strip().upper()[0]

    if idade >= 18:
        maiores_18 += 1

    if sexo == "M":
        homens_cadastrados += 1

    if ((sexo == "F") and (idade < 20)):
        mulheres_20 += 1
    
    lista_continuar = ["S", "N"]
    continuar = ""
    while continuar not in lista_continuar:
        continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

    contador_cadastro += 1

    if continuar != "S":
        break

print("\n--- Fim do(s) Cadastro(s) ---\n")

print(f"Pessoas com mais de 18 anos de idade: {maiores_18} pessoa(s)")
print(f"Homens cadastrados: {homens_cadastrados} homem(ns)")
print(f"Mulheres com menos de 20 anos de idade: {mulheres_20} mulher(es)")
