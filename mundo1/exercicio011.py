largura_parede = float(input("Digite a largura da parede (em m): "))
altura_parede = float(input("Digite a altura da parede (em m): "))
area = largura_parede * altura_parede
tinta = area / 2

print(f"Sua parede tem a dimensão de {largura_parede}x{altura_parede} com área de {area}m²")
print(f"Para pintar toda a parede, será preciso de {tinta}l de tinta")
