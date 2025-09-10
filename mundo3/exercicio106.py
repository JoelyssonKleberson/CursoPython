from time import sleep

cores = ('\033[m',        #0 - Sem cor
         '\033[0;30;41m', #1 - Vermelho
         '\033[0;30;42m', #2 - Verde
         '\033[0;30;43m', #3 - Amarelo
         '\033[0;30;44m', #4 - Azul
         '\033[0;37;45m', #5 - Roxo
         '\033[7;30m',    #6 - Branco
         )

def ajuda(opcao_usuario):
    print(cores[1], f"--- Comando \'{comando.upper()}\' ---" ,cores[0])
    print()
    help(comando)
    sleep(2)
    print()

comando = ""
while comando != "fim":
    print(cores[5], "--- Sistema de Ajuda - PyHELP ---", cores[0])
    comando = str(input("\nFunção ou Biblioteca: ")).strip().lower()
    print()
    if comando == "fim":
        break
    else:
        ajuda(comando)

print(cores[5], "--- Fim do Programa ---", cores[0],)
