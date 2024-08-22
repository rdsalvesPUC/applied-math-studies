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