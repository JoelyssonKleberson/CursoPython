tupla_palavras = ("comer", "jogar", "dormir", "casamento", "namorar", "academia", "futuro", "projeto", "evoluir")

for palavras in tupla_palavras:
    print(f"\nVogais na palavra \'{palavras.upper()}\' - ", end='')
    for letras in palavras:
        if letras.lower() in "aeiou":
            print(letras, end='')
    