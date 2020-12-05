# abrir o arquivo
# r - readonly
# w - re-write (clear e recreate)
# a - append
arquivo = open("files_example.txt")
#print(arquivo) # erro não printa objeto arquivos... precisa ler linhas


# array com todas as linhas
linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
    print("readlines: " + linha)

   
# linha a linha
arquivo.seek(0) # volta o ponteiro para o iníucio do arquivo
linha = arquivo.readline()

while linha:
    print("readline: " + linha)
    linha = arquivo.readline() # se nao houver mais nada para ser lido, a variável 'linha' retornará null (e a condicional while file irá falhar)

    
# string com textos das linhas
arquivo.seek(0) # volta o ponteiro para o iníucio do arquivo
texto = arquivo.read()
print("read: " + texto)


# criando arquivo e escrevendo (sempre um novo arquivo a cada chamada)
w1 = open("files_example_writeble.txt", "w")
w1.write("escrevendo uma nova linha no novo arquivo")

# alimentando arquivo para sempre
w2 = open("files_examples_rewriteble.txt", "a")
w2.write("adicionando uma nova linha\n")


arquivo.close()
w1.close()
w2.close()


"""
try:
    ar = open("f.txt")
except:    
    print("arquivo f.txt não existe. criando-o...")
    ar = open("f.txt", "w")
    ar.write("algo")
    ar.seek(0)
finally:    
    li = ar.readlines()
    print(li)
    ar.close()
"""

    
