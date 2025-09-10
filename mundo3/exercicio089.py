print("--- Alunos e Notas ---")

lista_dados = []
contador_alunos = 0
continuar = "S"
while continuar == "S":
    nome = str(input("\nNome: ")).capitalize()
    
    lista_notas = []
    notas = 2
    for quantidade_provas in range(2):
        notas = float(input(f"{quantidade_provas + 1}ª Nota: ").replace(",", "."))
        lista_notas.append(notas)

    media = sum(lista_notas) / len(lista_notas)
    lista_dados.append([nome, lista_notas, media])

    contador_alunos += 1
    continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

print("\n--- Boletim ---\n")

print("-"*33)
print(f"{"No.":<5}{"Nome:":<10}{"Média:":>10}")
print("-"*33)
for indice, aluno in enumerate(lista_dados):
    print(f"{indice + 1:<5}{aluno[0]:<10}{aluno[2]:>10.2f}")
print("-"*33)

ver_notas = str(input("\nDeseja ver as Notas Individuais (Sim ou Não)? ")).strip().upper()[0]
if ver_notas == "S":
    while ver_notas == "S":
        ver_notas_aluno = int(input("Digite a Numeração do Aluno: "))
        if ver_notas_aluno > contador_alunos or ver_notas_aluno <= 0:
            print("Número inválido!")
        elif ver_notas_aluno <= contador_alunos:
            print("\n--- Notas Individuais ---\n")
            print("-"*33)
            print(f"{"Aluno:":<10}{"Notas:"}")
            print("-"*33)
            print(f"{lista_dados[ver_notas_aluno - 1][0]:<10}{lista_dados[ver_notas_aluno - 1][1]}")
            print("-"*33)

            ver_notas = str(input("\nDeseja ver as Mais Notas Individuais (Sim ou Não)? ")).strip().upper()[0]

print("\n--- Fim do Processo ---")
