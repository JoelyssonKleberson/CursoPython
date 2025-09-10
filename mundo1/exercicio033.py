primeiro_valor = float(input("Digite o primeiro valor: "))
segundo_valor = float(input("Digite o segundo valor: "))
terceiro_valor = float(input("Digite o terceiro valor: "))

if ((primeiro_valor < segundo_valor) and (primeiro_valor < terceiro_valor)):
    menor_valor = primeiro_valor
elif ((segundo_valor < primeiro_valor) and (segundo_valor < terceiro_valor)):
    menor_valor = segundo_valor
elif ((terceiro_valor < primeiro_valor) and (terceiro_valor < segundo_valor)):
    menor_valor = terceiro_valor

if ((primeiro_valor > segundo_valor) and (primeiro_valor > terceiro_valor)):
    maior_valor = primeiro_valor
elif ((segundo_valor > primeiro_valor) and (segundo_valor > terceiro_valor)):
    maior_valor = segundo_valor
elif ((terceiro_valor > primeiro_valor) and (terceiro_valor > segundo_valor)):
    maior_valor = terceiro_valor

print(f"O menor valor digitado : {menor_valor}")
print(f"O maior valor digitado : {maior_valor}")
