peso_usuario = float(input("Digite o seu Peso (em kg): "))
altura_usuario = float(input("Digite a sua altura (em m): "))

imc = peso_usuario / altura_usuario ** 2

print(f"\nSeu IMC: {imc:.2f} kg/m²")
if imc < 18.5:
    print("Você está ABAIXO do Peso!")

elif ((imc >= 18.5) and (imc < 25)):
    print("Você está no Peso IDEAL!")

elif ((imc >= 25) and (imc < 30)):
    print("Você está com SOBREPESO!")

elif ((imc >= 30) and (imc < 40)):
    print("Você está com OBESIDADE!")

elif imc >= 40:
    print("Você está com OBESIDADE MÓRBIDA!")
