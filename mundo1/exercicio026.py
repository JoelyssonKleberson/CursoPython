frase_usuario = str(input("Digite uma frase: ")).strip().upper()
print(f"\nA letra 'A' apareceu {frase_usuario.count("A")} vez(es)")
print(f"A primeira letra 'A' apareceu na posição {frase_usuario.find("A") + 1}")
print(f"A última letra 'A' apareceu na posição {frase_usuario.rfind("A") + 1}")
