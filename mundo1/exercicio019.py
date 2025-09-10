from random import choice

aluno_1 = input("Digite o nome do Primeiro aluno: ")
aluno_2 = input("Digite o nome do Segundo aluno: ")
aluno_3 = input("Digite o nome do Terceiro aluno: ")
aluno_4 = input("Digite o nome do Quarto aluno: ")
lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
aluno_escolhido = choice(lista_alunos)

print(f"\nO aluno escolhido foi: {aluno_escolhido}")
