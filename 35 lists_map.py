# cria uma função
def retorna_dobro(x):
    return x*2

print(retorna_dobro(2))
print(retorna_dobro(5))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# se passar uma lista para função 'dobro',
#    não vai dobrar cada elemento, e sim vai dobrar a lista
print(retorna_dobro(lista))



# se quiser passar uma lista para função 'dobro',
#    mas que retorne o dobro para cada elemento, tem que usar 'map'
# map receber uma função e uma lista
lista_dobro = map(retorna_dobro, lista)
print(lista_dobro) # nao lista, pois é retornado um objetomap
print(list(lista_dobro))
