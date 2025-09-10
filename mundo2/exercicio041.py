from datetime import date
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = date.today().year
idade_atleta = ano_atual - ano_nascimento

if idade_atleta <= 9:
    print(f"\nIdade do Atleta: {idade_atleta} ano(s)")
    print("Sua Categoria é MIRIM!")

elif ((idade_atleta > 9) and (idade_atleta <= 14)):
    print(f"\nIdade do Atleta: {idade_atleta} anos")
    print("Sua Categoria é INFANTIL!")
    
elif ((idade_atleta > 14) and (idade_atleta <= 19)):
    print(f"\nIdade do Atleta: {idade_atleta} anos")
    print("Sua Categoria é JUNIOR!")

elif ((idade_atleta > 19) and (idade_atleta <= 25)):
    print(f"\nIdade do Atleta: {idade_atleta} anos")
    print("Sua Categoria é SÊNIOR!")

elif idade_atleta > 25:
    print(f"\nIdade do Atleta: {idade_atleta} anos")
    print("Sua Categoria é MASTER!")
