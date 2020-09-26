x = "Zé"
y = "Breu"

# concatenação simples
concatenar = x + " " + y
print (concatenar)

# tamanho
tamanho = len(concatenar)
print (tamanho)

# indice (0-index)
quintaletra = concatenar[4]
print(quintaletra)

# indice e tamanho (erro nao funcionou )
#quarta_e_quinta_letra = concatenar[1:3]
#quarta_e_quinta_letra = y[1:2]
#print(quarta_e_quinta_letra)

# minúsculo
low = concatenar.lower()
print(low)

# maiúsculo
upp = concatenar.upper()
print(upp)

# espaços (trim) e caracteres especiais no inicio e fim
x = " pqp \n"
print (x)
print (x.strip())

# dividir string em array
nova_lista = concatenar.split() # separator padrão é o espaço
print(nova_lista)
nova_lista_nova = "O rato roeu a roupa do rei de Roma".split("r")
print(nova_lista_nova)

# localizar índices de substrings
achou = concatenar.find("B")
print(achou) 
achou = concatenar.find("b") # case sensitive, vai retornar -1
print(achou)

# alterar textos
trocado = concatenar.replace("Breu", "Luiz")
print(trocado)
trocado = concatenar.replace("breu", "Luiz") # não vai achar
print(trocado)
