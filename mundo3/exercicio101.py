def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return (f"Idade: {idade} - NÃO vota!")
    elif ((idade >= 16 and idade < 18) or (idade > 65)):
        return (f"Idade: {idade} - Voto OPCIONAL!")
    else:
        return (f"Idade: {idade} - Voto OBRIGATÓRIO!")
    
print(voto(int(input("Digite o seu ano de Nascimento: "))))
