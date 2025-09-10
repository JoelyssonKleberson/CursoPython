velocidade_carro = int(input("Digite a velocidade em que seu carro está (em km/h): "))

if velocidade_carro > 80:
    print("\nVocê excedeu a velocidade de 80 km/h permitida")
    print(f"Sua multa será no valor de R$ {(velocidade_carro - 80) * 7:.2f}")
print("\nTenha um bom dia! Dirija com segurança e responsabilidade!")
