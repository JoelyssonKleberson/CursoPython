lista_pesos = []

for pesos in range(1, 6):
    peso_usuario = float(input(f"Digite o peso, em kg, da {pesos}ª pessoa: ").replace(",","."))
    lista_pesos.append(peso_usuario)

print(f"\nMaior peso: {max(lista_pesos):.2f} kg")
print(f"Menor peso: {min(lista_pesos):.2f} kg")
