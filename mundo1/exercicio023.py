numero_usuario = int(input("Digite um número inteiro entre 0 e 9999: "))
unidade = numero_usuario // 1 % 10
dezena = numero_usuario // 10 % 10
centena = numero_usuario // 100 % 10
milhar = numero_usuario // 1000 % 10

print(f"\nO número \'{numero_usuario}\' tem: ")
print(f"{milhar} Milhar(es)")
print(f"{centena} Centena(s)")
print(f"{dezena} Dezena(s)")
print(f"{unidade} Unidade(s)")
