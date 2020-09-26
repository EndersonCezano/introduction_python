# listas (arrays) podem ser de um tipo só ou de vários tipos
x = [1, 2, 3, 4, 5]
y = ["olá", "mundo", "!"]
z = [0, "olá", "biscoito", 9.99, True]


# buscar indíce
print(x[3])

# tamanho da lista
tam = len(y)
print(tam)

# adicionar elementos
x.append(6) # somente um argumento, adicionando sempre no final da lista
print(x)

x.insert(2, 9) # dois argumentos (índice, valor) adicionando 9 no índice 2
print(x)

# verificar existência
if 3 in x:
    print("3 existe na lista numérica")
    
if "oi" not in y:
    print("oi não existe na lista de string")

# removendo itens
del x[0]
print(x)

#del x[2:2] # nao funcionou
#print(x)

del x[2:]
print(x)

# limpar lista inteira
del x[:]
print(x)


# ordernar lista
a = [84, 94, 2323, 434, 56897, 32, 12, 3, 6, 0, 98]
b = ["bola", "abacate", "dinheiro"]

a1 = sorted(a)
print(a) # sorted altera a lista retornando uma nova
print(a1)

a.sort()
print(a) # sort já altera a lista original sem retorno
b.sort()
print(b) # ordem alfabétia
#z.sort() # erro: não e possível ordenar listas mistas
#print(z)

a.sort(reverse=True)
print(a)


# inverter posições
print(y)
y.reverse()
print(y)

