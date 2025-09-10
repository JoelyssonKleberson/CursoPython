print("--- LOJA TEM DE TUDO ---")

preco_compra = float(input("\nDigite o preço da(s) compra(s) (em R$): R$"))
print("\n--- Formas de Pagamento ---")
print("[ 1 ] - À Vista Dinheiro/Cheque")
print("[ 2 ] - À Vista Cartão")
print("[ 3 ] - Parcelado 2x no Cartão")
print("[ 4 ] - Parcelado 3x ou mais no Cartão\n")

opcao_usuario = str(input("Digite a sua opção (1, 2, 3 ou 4): "))
if opcao_usuario == "1":
    preco_compra -= (0.10 * preco_compra)

elif opcao_usuario == "2":
    preco_compra -= (0.05 * preco_compra)

elif opcao_usuario == "3":
    parcelas = preco_compra / 2

elif opcao_usuario == "4":
    parcelas_usuario = int(input("Digite a quantidade de Parcelas: "))
    preco_compra += 0.20 * preco_compra
    parcelas = preco_compra / parcelas_usuario

if opcao_usuario == "1" or opcao_usuario == "2":
    print(f"\nPreço da(s) compra(s): R${preco_compra:.2f} ")
elif opcao_usuario == "3":
    print(f"\nPreço das parceladas em 2x no cartão SEM JUROS: R${parcelas:.2f}")
elif opcao_usuario == "4":
    print(f"\nPreço das parceladas em {parcelas_usuario}x no cartão COM JUROS: R${parcelas:.2f}")
    print(f"Preço total da(s) compra(s): R${preco_compra:.2f}")
else:
    print("\nOpção Inválida!")