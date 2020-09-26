# definir funções sempre com a palavra reservada def
def soma_sem_retorno(a, b):
    print(a + b)

soma_sem_retorno(5, 4)


# retornando valor
def soma_com_retorno(a, b):
    return a + b

resultado = soma_com_retorno(5, 4)
print(resultado)


# recursivo
def multiplicacao_com_retorno(a, b):
    return a + b

s = soma_com_retorno(5, 4)
m = multiplicacao_com_retorno(9, 5)
print(soma_com_retorno(s, m))


# funcoes devem ser declaradas antes de usar senao não reconhece (igual delphi)
