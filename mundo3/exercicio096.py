def calculo_area_terreno():
    largura = float(input("Largura (m): "))
    comprimento = float(input("Comprimento (m): "))
    area = largura * comprimento

    print(f"A área do terreno {largura}m x {comprimento}m é de {area:.2f}m²")  
    
calculo_area_terreno()
