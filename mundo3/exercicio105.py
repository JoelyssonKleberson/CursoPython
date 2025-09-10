def media_notas(lista):
    notas_alunos['Total'] = len(lista)
    notas_alunos['Maior'] = max(lista)
    notas_alunos['Menor'] = min(lista)
    notas_alunos['Média'] = sum(lista) / len(lista)

    if notas_alunos['Média'] >= 7:
        notas_alunos['Situação'] = "Boa!"
    elif ((notas_alunos["Média"] < 7) and (notas_alunos['Média'] >= 5)):
        notas_alunos['Situação'] = "Razoável!"
    elif notas_alunos['Média'] < 5:
        notas_alunos['Situação'] = "Ruim!"

    return notas_alunos
    
notas_alunos = {}
lista_numeros = [7.5, 9.0, 9.5]
media_notas(lista_numeros)
print(notas_alunos)
