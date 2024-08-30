import matplotlib.pyplot as plt
import numpy as np
import math

def funcao1Grau(a,b,x):
	return(a*x+b)

def funcao2Grau(a,b,c,x):
	return(a * (pow(x,2)) + b * x + c)

def fooExponencial(a,b,x):
	return(a * pow(b, x))

def fooModular(x):
	return abs(x)

def fooSeno(x):
	return math.sin(x)

vetorX = np.arange(-5,5,1)
print(vetorX)

a = 2
b = 5
c = 1

vetorY = []

for i in vetorX:
	# vetorY.append(int(funcao1Grau(a,b,i)))
	# vetorY.append(int(funcao2Grau(a,b,c,i)))
	# vetorY.append(int(fooExponencial(a,b,i)))
	# vetorY.append(int(fooModular(i)))
	vetorY.append(int(fooSeno(i)))

	
print(vetorY)


fig = plt.figure(figsize=(10,10))
# plt.scatter(vetorX, vetorY, label = "Função 2o Grau")
# plt.scatter(vetorX, vetorY, label = "Função Exponencial")
# plt.scatter(vetorX, vetorY, label = "Função Modular")
plt.scatter(vetorX, vetorY, label = "Função Seno")
# plt.title('f(x)=ax+b')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()