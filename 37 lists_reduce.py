# importar biblioteca
from functools import reduce

# cria uma função
def soma(x, y):
	return x+y

lista = [1, 3, 5, 10, 20]


soma = reduce(soma, lista)
print(soma)