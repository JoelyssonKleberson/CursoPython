nome_completo = str(input("Digite o seu nome completo: ")).strip()

print(f"\nSeu nome em letras MAIÚSCULAS: {nome_completo.upper()}")
print(f"Seu nome em letras MINÚSCULAS: {nome_completo.lower()}")
print(f"Seu nome tem um total de {len(nome_completo) - nome_completo.count(' ')} letras")

primeiro_nome = nome_completo.split()
print(f"Seu primeiro nome \'{primeiro_nome[0].capitalize()}\' tem {len(primeiro_nome[0])} letras")
