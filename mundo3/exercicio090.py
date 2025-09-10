print("--- Dados Aluno ---\n")
aluno = {}
aluno['Nome'] = str(input("Nome: ")).capitalize()
aluno['Média'] = float(input("Média: ").replace(",", "."))

if aluno['Média'] >= 7:
    aluno['Situação'] = "Aprovado!"
elif aluno['Média'] < 7 and aluno['Média'] >= 5:
    aluno['Situação'] = "Recuperação!"
elif aluno['Média'] < 5:
    aluno['Situação'] = "Reprovado!"

print("\n--- Boletim ---\n")
for keys, chaves in aluno.items():
    print(f"{keys}: {chaves}")
