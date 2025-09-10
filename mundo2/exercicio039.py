from datetime import date
ano_nascimento = int(input("Digite o ano de seu nascimento: "))

ano_atual = date.today().year
idade_alistamento = ano_atual - ano_nascimento

if idade_alistamento < 18:
    print(f"\nIdade: {idade_alistamento} ano(s)")
    tempo_alistamento = 18 - idade_alistamento
    print(f"Tempo para o Alistamento: {tempo_alistamento} ano(s)")
    print(f"Ano de Alistamento: {ano_atual + tempo_alistamento}")

elif idade_alistamento == 18:
    print(f"\nIdade: {idade_alistamento} ano(s)")
    print("Você deve se Alistar IMEDIATAMENTE!")

elif idade_alistamento > 18:
    print(f"\nIdade: {idade_alistamento} ano(s)")
    tempo_alistamento = idade_alistamento - 18
    print(f"Você deveria ter se AListado há {tempo_alistamento} ano(s)")
    print(f"Ano de Alistamento: {ano_atual - tempo_alistamento}")
