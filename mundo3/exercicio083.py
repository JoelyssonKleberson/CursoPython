#Solução de Guanabara
expressao_usuario = str(input("Digite uma expressão com \'( )\': "))
pilha_parenteses = []

for parentes in expressao_usuario:
    if parentes == '(':
        pilha_parenteses.append('(')
    elif parentes == ')':
        if len(pilha_parenteses) > 0:
            pilha_parenteses.pop()
        else:
            pilha_parenteses.append(')')
            break
    
if len(pilha_parenteses) == 0:
    print("Sua expressão está VÁLIDA!")
else:
    print("Sua expressão NÃO está válida!")

#Minha solução.
expressao_usuario = str(input("\nDigite: "))
parenteses_abrindo = parenteses_fechando = 0

for expressao in expressao_usuario:
    if expressao == "(":
        parenteses_abrindo += 1
    elif expressao == ")":
        parenteses_fechando += 1

if parenteses_abrindo == parenteses_fechando:
    print("Sua expressão está VÁLIDA!")
else:
    print("Sua expressão NÃO está válida!")
