# 10) Faça um menu que só encerre quando o usuário solicitar (opção de sair) que seja interativo e com as devidas validações de possíveis erros de entrada do usuário. O objetivo é fazer a operação entre 2 conjuntos, ou seja, crie uma forma de pedir dois conjuntos para o usuário (conjuntos A e B – posteriormente esses conjuntos podem ser alterados pelo usuário). As opções de operações são:
# a) União
# b) Intersecção
# c) Diferença
# d) Produto cartesiano
# d) Verificação se A é subconjunto de B (submenu: subconjunto ou subconjunto próprio)
# e) Mesma verificação do item d, mas de B com A.
def uniao(conjuntoX, conjuntoY):
    return conjuntoX.union(conjuntoY)

def intersecao(conjuntoX, conjuntoY):
    return conjuntoX.intersection(conjuntoY)

def diferenca(conjuntoX, conjuntoY):
    return conjuntoX.difference(conjuntoY)

def produto_cartesiano(conjuntoX, conjuntoY):
    return set([(x, y) for x in conjuntoX for y in conjuntoY])

def isSubconjunto(conjuntoX, conjuntoY):
    return conjuntoX.issubset(conjuntoY)

def isSubconjuntoProprio(conjuntoX, conjuntoY):
    if conjuntoX.issubset(conjuntoY) and conjuntoX != conjuntoY:
        return True
    else:
        return False

def isAlpha(entrada_dados):
    for char in entrada_dados:
        if char.isalpha():
            return True

def parseStrToConjunto(string):
    isAlpha(string)
    # limpar os espaços em branco
    # conver
    
def operacoes(option, conjuntoX, conjuntoY):
    match option:
        case 1:
            uniao(conjuntoX, conjuntoY)
        case 2:
            intersecao(conjuntoX, conjuntoY)
        case 3:
            diferenca(conjuntoX, conjuntoY)
        case 4:
            produto_cartesiano(conjuntoX, conjuntoY)
        case 5:
            isSubconjunto(conjuntoX, conjuntoY)
        case 6:
            isSubconjuntoProprio(conjuntoX, conjuntoY)

def main():
    while True:
        option = input(print('Digite a opção desejada: '))

        if option == 7:
            print('Finalizando o programa...')
            break

        if option in [1,2,3,4,5,6]:
            stringX = input(print('Digite os valores para o conjunto A (separados por virgula)'))
            stringY = input(print('Digite os valores para o conjunto B (separados por virgula)'))
        
        if isAlpha(stringX):
            break
        else:
            conjuntoX = parseStrToConjunto(stringX)
            
        if isAlpha(stringY):
            break
        else:
            conjuntoY = parseStrToConjunto(stringY)

        
        operacoes(option, conjuntoX, conjuntoY)
                    
main()