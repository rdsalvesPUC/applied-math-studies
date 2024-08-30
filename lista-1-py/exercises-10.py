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
    valores = string.split(',')
    conjunto = {int(valor) for valor in valores}

    return conjunto
    
def operacoes(option, conjuntoX, conjuntoY):
    match option:
        case 1:
            resultado = uniao(conjuntoX, conjuntoY)
            resposta = "A união dos conjuntos resultou no conjunto: " + str(resultado)
        case 2:
            resultado = intersecao(conjuntoX, conjuntoY)
            resposta = "A interseção dos conjuntos resultou no conjunto: " + str(resultado)
        case 3:
            resultado = diferenca(conjuntoX, conjuntoY)
            resposta = "A diferença dos conjuntos resultou no conjunto: " + str(resultado)
        case 4:
            resultado = produto_cartesiano(conjuntoX, conjuntoY)
            resposta = "O Produto Cartesiano dos conjuntos resultou no conjunto: " + str(resultado)
        case 6:
            resultado = isSubconjuntoProprio(conjuntoX, conjuntoY)
            resposta = "O Conjunto A é subconjunto do Conjunto B?: " + str(resultado)
    
    return resposta

def main():
    while True:
        option = int(input('Digite a opção desejada: '))

        if option == 7:
            print('Finalizando o programa...')
            break

        if option in [1,2,3,4,5,6]:
            stringX = input('Digite os valores para o conjunto A (separados por virgula)')
            stringY = input('Digite os valores para o conjunto B (separados por virgula)')
        
        if isAlpha(stringX):
            print('Não utilize letras, somente valores numéricos')
            break
        else:
            conjuntoX = parseStrToConjunto(stringX)
            # print(conjuntoX)
            
        if isAlpha(stringY):
            print('Não utilize letras, somente valores numéricos')
            break
        else:
            conjuntoY = parseStrToConjunto(stringY)
            # print(conjuntoY)

        resposta = operacoes(option, conjuntoX, conjuntoY)

        print(resposta)
                    
main()