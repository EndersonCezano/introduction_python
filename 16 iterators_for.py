# listas podem ser de um tipo só ou de vários tipos
x = [1, 2, 3, 4, 5]
y = ["olá", "mundo", "!"]
z = [0, "olá", "biscoito", 9.99, True]

for i in x:
    print(i)

for i in y:
    print(i)

for i in z:
    print(i)

# range cria uma nova lista
# lista são 0-index

for i in range(10):  # total de elementos que ser quer na lista
    print(i)

for i in range(10, 20): # valor de origem e valor fim
    print(i)


for i in range(10, 20, 2): # valor de origem e fim, e valor do passo
    print(i)
