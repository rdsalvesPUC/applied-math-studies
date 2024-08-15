# As respostas devem ser um print do código e da saída em python

# 1) Vamos criar um conjunto:
# A = {1,2,3,4,5,6}
# print(A)
# Saída:
A = {1,2,3,4,5,6}
print(frozenset() in A)


# 2) Vamos criar um conjunto a partir de uma lista
# lista = [“bananas”, “peras”, “laranjas”, “abacates”]
# B = set(lista)
# print(B)
# Saída:
lista = ['bananas', 'peras', 'laranjas', 'abacates']
B = set(lista)
print(B)


# 3) Seguindo a mesma lógica do item anterior:
# lista = [“bananas”, “peras”, “laranjas”, “limões”, “bananas”, “bananas”, “abacates”, “laranjas”]
# B = set(lista)
# print(B)
# Saída:
lista = ['bananas', 'peras', 'laranjas', 'limões', 'bananas', 'bananas', 'abacates', 'laranjas']
B = set(lista)
print(B)
# Comparando os itens 2 e 3, a que conclusão podemos chegar?
# Resposta:
# Que uma lista pode conter infinitos valores, mas um set, só pode ter valores únicos não repetidos.


# 4) Imprima a cardinalidade do conjunto B obtido no item 3 da forma: “A cardinalidade do conjunto B = { ... } é {tamanho}”
# Dica: utilize a palavra reservada do python “len”
# Resposta:
print(len(B))

# 5) Teste as relações de pertinência e imprima a resposta (A = {1,2,3,4,5})
# Dica: utilize a palavra reservada do python “in”
# a)
# b)
# c)
A = {1,2,3,4,5}
reposta = 'True' if 2 in A else 'False'
print(reposta)
reposta = 'True' if 6 in A else 'False'
print(reposta)
reposta = 'True' if frozenset() in A else 'False'
print(reposta)


# 6) Teste a igualdade entre os conjuntos A= {1,2,3} e B = {3,2,1}, A é igual a B? Imprima o resultado
A= {1,2,3}
B = {3,2,1}

resposta = 'True' if A == B else 'False'
print(resposta)


# 7) Utilize a função issubset() para testar todos os subconjuntos de C = {2,3,4} – imprima os resultados
# Agora, faça o teste utilizando o operador de pertinência em python para o seguinte exemplo:
def criarSubconjuntos(conjunto):
  subconjuntos = []

  subconjuntos.append(frozenset())

  for i in conjunto:
    subconjuntos.append(set([i]))

  for i in conjunto:
    for j in conjunto:
      if i != j:
        if set([i, j]) not in subconjuntos:
          subconjuntos.append(set([i, j]))

  subconjuntos.append(set(conjunto))
  return subconjuntos

C = {2, 3, 4}

subconjuntos = criarSubconjuntos(C)

for subconjunto in subconjuntos:
    print(f"{subconjunto} é subconjunto de C: {subconjunto.issubset(C)}")

# Qual resultado é esperado? O python respeita esse resultado?
# O esperado era que fosse False, e sim o python respeita
# {1,2} é um subconjunto, e um subconjunto não pode pertencer a um conjunto.
# Faça o teste para o conjunto vazio:

# Qual resultado é esperado? O python respeita esse resultado?
# O conjunto vazio é um subconjunto de A. Ele não é um elemento isolado para pertencer a A

# 8) Crie uma verificação para testar se A = {1,2,3} é subconjunto próprio de C = {1,2,3,4,5} – imprima o código e resultado. Agora reaproveite o código para testar se D = {5,3,4,2,1} é subconjunto próprio de C.
A = {1,2,3}
C = {1,2,3,4,5}
D = {5,3,4,2,1}

def isSubconjuntoProprio(conjuntoX, conjuntoY):
  if conjuntoX.issubset(conjuntoY) and conjuntoX != conjuntoY:
    return True
  else:
    return False

print(isSubconjuntoProprio(A, C))
print(isSubconjuntoProprio(D, C))


# 9) Considerando: A = {1,2,3,4,5} e B = {4,5,6,7,8,9,10} faça a conta (mostrando a simbologia matemática e imprima os resultados em python):
# a)
# b)
# c) A – B
# d) B – A
A = {1,2,3,4,5}
B = {4,5,6,7,8,9,10}

def uniao(conjuntoX, conjuntoY):
  return conjuntoX.union(conjuntoY)

def intersecao(conjuntoX, conjuntoY):
  return conjuntoX.intersection(conjuntoY)

def diferenca(conjuntoX, conjuntoY):
  return conjuntoX.difference(conjuntoY)

print(uniao(A, B))
print(intersecao(A, B))
print(diferenca(A, B))
print(diferenca(B, A))


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

while True:
  option = input(print('''
        ## Digite o número da opção desejada:
        1) União
        2) Intersecção
        3) Diferença
        4) Produto cartesiano
        5) Verificação se A é subconjunto de B (submenu: subconjunto ou subconjunto próprio)
        6) Mesma verificação do item d, mas de B com A.
        7) Sair'''))
  if option == 7:
    break
