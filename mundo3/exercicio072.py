numeros_extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
                   "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

numero_usuario = None
while ((numero_usuario is None) or (numero_usuario < 0) or (numero_usuario > 20)):
    numero_usuario = int(input("Digite um número entre 0 e 20: "))
    if ((numero_usuario < 0) or (numero_usuario > 20)):
        print("Número inválido!")

print()

#Minhas formas

#Primeira Forma
for numero in numeros_extenso[numero_usuario]:
    print(f"{numero}", end='')

#Segunda Forma
lista_numeros = []
for numero in numeros_extenso[numero_usuario]:
    lista_numeros.append(numero)

numero_extenso_usuario = ''.join(lista_numeros)
print(f"\n{numero_extenso_usuario}")

#Forma Infinitamente mais fácil (Guanabara)
print(f"Você digitou o número \'{numeros_extenso[numero_usuario]}\'")
