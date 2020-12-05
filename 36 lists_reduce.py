# cria uma função
def retorna_pares(i):
    if (i % 2 == 0):
        return i

print(retorna_pares(2))
print(retorna_pares(5))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# funcao filter espera uma função e uma lista,
# a função deve ter, necessariamente um atributo inteiro, como criado acima
lista_pares = filter(retorna_pares, lista)

# precisa converter o retorno
lista_pares_convertida = list(lista_pares)
print(lista_pares_convertida)
