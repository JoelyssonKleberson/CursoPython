distancia = int(input("Digite a distância da viagem (em km): "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Sua preço da sua passagem será de R$ {preco:.2f}")
