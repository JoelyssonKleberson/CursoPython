def arquivo_existe(nome):
    try:
        abrir_arquivo = open(nome, 'rt+')
        abrir_arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        abrir_arquivo = open(nome, 'wt+')
        abrir_arquivo.close()
    except:
        print(f"'\n\033[31m',Houve um Erro na \'Criação\' do Arquivo \'{nome}\'!",'\033[m')
    else:
        print(f"Arquivo \'{nome}\' criado!")
        
def ler_arquivos(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('\n\033[31m',"Erro ao \'Ler\' o Arquivo!",'\033[m')
    else:
        print("-"*30)
        print("--- Pessoas Cadastradas ---".center(30))
        print("-"*30)
        print(f"{"Nome:":<25}{"Idade:":>3}")
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<25}{dado[1]:>2} anos")
        print("-"*30)
    finally:
        arquivo.close()

def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31m',"Opção Inválida!",'\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m',"Entrada de Dados \'Não Informada\' pelo Usuário!",'\033[m')
            return 0
        else:
            return numero
        
def cadastrar(arquivo, nome = 'Desconhecido', idade = 0):
    try:
        cadastrar_arquivo = open(arquivo, 'at')
    except:
        print('\n\033[31m',"Erro na \'Abertura\' do Arquivo!",'\033[m')
    else:
        try:
            cadastrar_arquivo.write(f"{nome};{idade}\n")
        except:
            print('\n\033[31m',"Erro na hora de \'Escrever\' os Dados!",'\033[m')
        else:
            print(f"Novo Registro: {nome} adicionado(a)!")
            cadastrar_arquivo.close()