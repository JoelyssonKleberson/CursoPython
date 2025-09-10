from math import hypot

cateto_oposto = float(input("Digite a medida do Cateto Oposto: "))
cateto_adjacente = float(input("Digite a medida do Cateto Adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"\nA Hipotenusa será de: {hipotenusa:.2f}")
