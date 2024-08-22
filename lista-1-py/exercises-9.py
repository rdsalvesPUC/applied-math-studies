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