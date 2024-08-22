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
    
def main():
	while True:
		option = int(input(print('''
## Digite o número da operação desejada:
	1) União
	2) Intersecção
	3) Diferença
	4) Produto cartesiano
	5) Verificação se A é subconjunto de B (submenu: subconjunto ou subconjunto próprio)
	6) Mesma verificação do item d, mas de B com A.
	7) Sair''')))
        
		if option == 7:
			print('Finalizando o programa...')
			break
        
		if option in [1,2,3,4,5,6]:
			conjuntoX = print('')
			conjuntoY = print('')
            
			match option:
				case 1:
					uniao(conjuntoX, conjuntoY)
				case 2:
					intersecao(a,b)
				case 3:
					diferenca(a, b)
				case 4:
					produto_cartesiano(a, b)
				case 5:
					isSubconjunto(a, b)
				case 6:
					isSubconjuntoProprio(a, b)

main()