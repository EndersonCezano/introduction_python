
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["fruta", "objeto", "animal", "objeto", "animal"]

# zip é para alinhar um elemento de uma lista com outro
#  elemento de outra lista, na mesma posição
print(list(zip(lista1, lista2)))
for i, nome in zip(lista1, lista2):
    print(i, nome)


# zip pode ser usado em quantas listas quiser
print(list(zip(lista1, lista2, lista3)))
for i, nome, tipo in zip(lista1, lista2, lista3):
    print(i, nome, tipo)



# se a primeira lista tiver mais elementos, eles serão ignorados
x = [0, 1, 2]
y = ["a", "b"]
print(list(zip(x, y)))


# se a segunda lista tiver mais elementos, eles serão ignorados
x = [0, 1]
y = ["a", "b", "c"]
print(list(zip(x, y)))

