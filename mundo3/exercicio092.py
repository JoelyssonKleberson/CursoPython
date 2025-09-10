from datetime import date

cadastro_trabalhador = {}
cadastro_trabalhador['nome'] = str(input("Nome: ")).strip().capitalize()
idade = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
cadastro_trabalhador['idade'] = ano_atual - idade
cadastro_trabalhador['carteira de trabalho'] = int(input("Carteira de Trabalho (0 se não tiver): "))

if cadastro_trabalhador['carteira de trabalho'] != 0:
    cadastro_trabalhador['ano de contratação'] = int(input("Ano de Contratação: "))
    cadastro_trabalhador['salario'] = float(input("Salário: R$"))
    cadastro_trabalhador['aposentadoria'] = cadastro_trabalhador['idade'] + (cadastro_trabalhador['ano de contratação'] + 35) - ano_atual

print("\n--- Dados ---\n")
for dados, dados_usuario in cadastro_trabalhador.items():
    print(f"{dados}: {dados_usuario}")
