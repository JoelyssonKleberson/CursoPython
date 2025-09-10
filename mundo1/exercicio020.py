from random import shuffle

aluno_1 = input("Digite o nome do Primeiro aluno: ")
aluno_2 = input("Digite o nome do Segundo aluno: ")
aluno_3 = input("Digite o nome do Terceiro aluno: ")
aluno_4 = input("Digite o nome do Quarto aluno: ")
lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos)
print(f"\nA ordem de apresentação será: \n{lista_alunos}")
