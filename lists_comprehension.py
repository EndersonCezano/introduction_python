# criando uma nova lista com os quadrados das listas
x = [1 ,2 ,3 ,4 ,5]

# **********
# formula básica (varre a lista original e adiciona valores na lista adicional)
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)


# **********
# formula do python (list comprehension)
#       y = [valor_a_adicionar laço condição]
#           laço = for i in x
#           valor_a_adicionar = i ** 2 (i² de cada valor da lsita original)
#           condição = não há (neste exemplo)

y = [i**2 for i in x]
print(x)
print(y)


# **********
# formula do python (list comprehension) com uma condição (apenas valores ímpares)
#       y = [valor_a_adicionar laço condição]
#           laço = for i in x
#           valor_a_adicionar = i (sem tratamento, apenas retornar os valores)
#           condição = if (i%2 == 1) (resto igual 0, valor e par, e igual 1 é ímpar)

z = [(i) for i in x if (i%2 == 1)]
print(x)
print(z)
