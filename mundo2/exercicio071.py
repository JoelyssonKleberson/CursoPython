print("--- Caixa Eletrônico ---\n")
print("Notas Disponíveis:")
print("R$50 - R$20 - R$10 - R$1\n")

nota_50 = nota_20 = nota_10 = moeda_1 = 0

saque = int(input("Digite o valor do saque: R$"))
if saque >= 50:
    nota_50 = saque // 50 
    saque = saque % 50

if saque >= 20:
    nota_20 = saque // 20
    saque = saque % 20

if saque >= 10:
    nota_10 = saque // 10
    saque = saque % 10

if saque >= 1:
    moeda_1 = saque // 1
    saque = saque % 1

print("\n--- Notas e/ou Moedas ---\n")

if nota_50 > 0:
    print(f"{nota_50} nota(s) de R$50,00")
if nota_20 > 0:
    print(f"{nota_20} nota(s) de R$20,00")
if nota_10 > 0:
    print(f"{nota_10} nota(s) de R$10,00")
if moeda_1 > 0:
    print(f"{moeda_1} moeda(s) de R$1,00")
