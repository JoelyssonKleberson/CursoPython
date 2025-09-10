primeira_nota = float(input("Digite a Primeira Nota: "))
segunda_nota = float(input("Digite a Segunda Nota: "))
media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print(f"\nMédia: {media:.2f}")
    print("Aluno REPROVADO!")

elif ((media >= 5) and (media <= 6.9)):
    print(f"\nMédia: {media:.2f}")
    print("Aluno está em RECUPERAÇÃO!")

elif media >= 7:
    print(f"\nMédia: {media:.2f}")
    print("Aluno APROVADO!")