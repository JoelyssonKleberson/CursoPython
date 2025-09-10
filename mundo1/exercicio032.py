from datetime import date
ano_usuario = int(input("Digite o ano que deseja analisar ou digite \'0\' para o ano atual: "))

if ano_usuario == 0:
    ano_usuario = date.today().year

if ((ano_usuario % 4 == 0 and ano_usuario % 100 != 0) or (ano_usuario % 400 == 0)):
    print(f"O ano de \'{ano_usuario}\' é BISSEXTO")
else:
    print(f"O ano de \'{ano_usuario}\' NÃO é BISSEXTO")
