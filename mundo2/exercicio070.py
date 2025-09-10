lista_preco = []
produto_1000 = 0
produto_barato = None
nome_produto_barato = ""

print("--- LOJA TEM DE TUDO ---")

while True:
    nome_produto = str(input("\nDigite o Nome do Produto: "))
    preco_produto = float(input("Digite o Preço do Produto: R$"))

    lista_preco.append(preco_produto)

    if preco_produto > 1000:
        produto_1000 += 1

    if produto_barato is None or preco_produto < produto_barato:
        nome_produto_barato = nome_produto
        produto_barato = preco_produto

    lista_continuar = ["S", "N"]
    continuar = ""
    while continuar not in lista_continuar:
        continuar = str(input("Deseja continuar (Sim ou Não)? ")).strip().upper()[0]

    if continuar != "S":
        break

print("\n--- FIM DO PROGRAMA ---\n")

print(f"Preço total da(s) compra(s): R${sum(lista_preco):.2f}")
print(f"Produtos custando mais de R$1.000,00: {produto_1000} produto(s)")
print(f"Produto mais barato: {nome_produto_barato}, R${produto_barato:.2f}")
