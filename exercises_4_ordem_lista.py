print("\n\n************ Exercício #4 ************")
lista = []
try:
    a_str = input("Digite um número: ")
    a = float(a_str.strip().replace(",", "."))
    lista.append(a)

    b_str = input("Digite um número de novo: ")
    b = float(b_str.strip().replace(",", "."))
    lista.append(b)

    c_str = input("Digite um número só mais uma vez: ")
    c = float(c_str.strip().replace(",", "."))
    lista.append(c)

    lista.sort()
    print(lista)
    
except:
    print("Valor inválido. Abortando exercício...")




