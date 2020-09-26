x = ["coelho", "cobra", "sapo", "aranha"]

print(list(enumerate(x)))

# i é o valor de cada elemento
for i in x:
    print(i)

# i é o valor do índice
for i in range(len(x)):
    #print(str(i) + " " + str(x[i]))
    print("range/len", i, x[i]) # dessa forma nao precisa converter para string


# enumerate já traz o índice e nome sem precisar do range/len
for i, nome in enumerate(x):
    print("enumerate", i, nome)
