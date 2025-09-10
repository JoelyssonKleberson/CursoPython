from time import sleep

def contagem_crescente():
    print("--- Contagem de 1 até 10 de 1 em 1 ---")
    for numero in range(1, 11):
        print(f"{numero}", end=' ')
        sleep(0.5)
    print("Fim!")


def contagem_regressiva():
    print("\n--- Contagem Regressiva de 10 até 0 de 2 em 2 ---")
    for numero in range(10, -1, -2):
        print(f"{numero}", end=' ')
        sleep(0.5)
    print("Fim!")


def contagem_personalizada():
    print(f"\n--- Contagem Personalizada ---")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))

    print(f"\n--- Contagem Personalizada de {inicio} até {fim} de {passo} em {passo} ---")

    if passo >= 0:
        passo = 1
        for numero in range(inicio, fim + 1, passo):
            print(f"{numero}", end=' ')
            sleep(0.5)
        print("Fim!")
    
    elif passo < 0:
        if (inicio < 0 and passo < 0) or (inicio < 0 and fim < 0) or (passo < 0 and fim < 0):
            passo *= -1
            for numero in range(inicio, fim + 1, passo):
                print(f"{numero}", end=' ')
                sleep(0.5)
            print("Fim!")
        else:
            passo *= -1
            for numero in range(inicio, fim - 1, passo):
                print(f"{numero}", end=' ')
                sleep(0.5)
            print("Fim!")

contagem_crescente()
contagem_regressiva()
contagem_personalizada()
