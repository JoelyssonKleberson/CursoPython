soma_impares = 0
contador_impares = 0
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        contador_impares += 1
        soma_impares += soma
    
print(f"A soma dos {contador_impares} números é \'{soma_impares}\'")
