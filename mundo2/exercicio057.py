sexo = ""
lista_sexos = ["M", "F"]
while sexo not in lista_sexos:
    sexo = str(input("Digite o seu sexo (M ou F): ")).strip().upper()[0]
    if sexo not in lista_sexos:
        print("Sexo inválido!")

if sexo == "M":
    print("\nSexo \'Masculino\' registrado!")
else:
    print("\nSexo \'Feminino\' registrado!")
