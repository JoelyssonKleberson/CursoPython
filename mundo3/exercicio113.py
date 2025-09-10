def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31m',"Opção Inválida! Digite um valor INTEIRO!",'\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m',"Entrada de Dados \'Não Informada\' pelo Usuário!",'\033[m')
            return 0
        else:
            return numero
        
def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31m',"Opção Inválida! Digite um valor REAL!",'\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m',"Entrada de Dados \'Não Informada\' pelo Usuário!",'\033[m')
            return 0
        else:
            return numero

numero_inteiro = leiaInt("Digite um numero Inteiro: ")
numero_real = leiaFloat("Digite um numero Real: ")
print(f"\nNuméro \'Inteiro\': {numero_inteiro}")
print(f"Numéro \'Real\': {numero_real}")
