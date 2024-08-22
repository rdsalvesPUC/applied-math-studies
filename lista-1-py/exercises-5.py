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