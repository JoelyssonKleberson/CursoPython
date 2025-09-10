salario_funcionario = float(input("Digite o salário do funcionário: R$"))
if salario_funcionario <= 1250:
    salario_funcionario += 0.15 * salario_funcionario
elif salario_funcionario > 1250:
    salario_funcionario += 0.10 * salario_funcionario

print(f"O novo salário será de R${salario_funcionario:.2f}") 
