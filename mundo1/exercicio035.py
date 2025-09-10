reta_1 = float(input("Digite o primeiro segmento: "))
reta_2 = float(input("Digite o segunda segmento: "))
reta_3 = float(input("Digite o terceiro segmento: "))

if ((reta_1 < reta_2 + reta_3) and (reta_2 < reta_1 + reta_3) and (reta_3 < reta_1 + reta_2)):
    print("Os segmentos mencionados PODEM formar um triângulo!")
else:
    print("Os segmentos mencionados NÃO PODEM formar um triângulo!")
    