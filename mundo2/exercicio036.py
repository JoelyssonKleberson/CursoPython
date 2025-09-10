valor_casa = float(input("Digite o valor da casa (em R$): R$"))
salario_comprador = float(input("Digite o salário do comprador (em R$): R$"))
quantidade_anos = int(input("Digite a tempo (em anos) para pagar: "))

meses = quantidade_anos * 12
valor_prestacao = valor_casa / meses

if valor_prestacao > (0.30 * salario_comprador):
    print("\nEmpréstimo NEGADO!")
    exit()

print("\nEmpréstimo ACEITO!")
print(f"Prestação: R${valor_prestacao:.2f}")
