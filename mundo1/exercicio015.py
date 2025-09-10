dias_alugado = int(input("Quantos dias foi alugado? "))
quilometros = float(input("Digite a quantidade de km rodados: "))
valor_pagar = (dias_alugado * 60) + (0.15 * quilometros)

print(f"O valor a pagar será de R${valor_pagar:.2f}")
