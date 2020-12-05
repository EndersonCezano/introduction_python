print("\n\n************ Exercício #5 ************")
try:
    a_str = input("Digite um número: ")
    a = float(a_str.strip().replace(",", "."))

    b_str = input("Digite um número de novo: ")
    b = float(b_str.strip().replace(",", "."))

    operator = input("Agora informe uma operação. Digite um dos seguintes sinais (+ - * /): ").strip()
    if (operator == "+"):
        print("Resultado da adição: " + str(a + b))
    elif (operator == "-"):
        print("Resultado da subtração: " + str(a - b))
    elif (operator == "*"):
        print("Resultado da multiplicação: " + str(a * b))
    elif (operator == "/"):
        print("Resultado da divisão: " + str(a / b))
    else:
        print("Operador inválido. Abortando exercício...")
    
except:
    print("Valor inválido. Abortando exercício...")
