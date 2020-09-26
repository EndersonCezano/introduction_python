print("************ Exercício #1 ************")
idade_str = input("Digite sua idade: ")
try:
    idade = int(idade_str.strip())
except:
    idade = 0
    
if (idade <= 0):
    print("Idade informada é inválida.")
elif (idade < 18):
    print("Você é menor de idade.")
elif (idade > 60):
    print("Você já é idoso")
else:
    print("Você é maior de idade.")







print("\n\n************ Exercício #2 ************")
nota1_str = input("Digite a primeira nota (decimal de 0 a 10): ")
try:
    nota1 = float(nota1_str.strip().replace(",", "."))
except:
    nota1 = -1

if (nota1 < 0 or nota1 > 10):
    print("Primeira nota é inválida. Abortando exercício...")
    
else:    
    nota2_str = input("Digite a segunda nota (decimal de 0 a 10): ")
    try:
        nota2 = float(nota2_str.strip().replace(",", "."))
    except:
        nota2 = -1

    if (nota2 < 0 or nota2 > 10):
        print("Segunda nota é inválida. Abortando exercício...")

    else:
        media = (nota1 + nota2) / 2
        print("Média final: " + str(media))

        if (media >= 6):
            print("Resultado final: Aprovado")
        else:
            print("Resultado final: Reprovado")






import math
print("\n\n************ Exercício #3 ************")
print("Equação do 2º grau: ax² + bx + c = 0")
a_str = input("Digite valor de A: ")
try:
    a = float(a_str.strip().replace(",", "."))
except:
    a = 0

if (a == 0):
    print("Valor de A é inválido. Abortando exercício...")
    
else:    
    b_str = input("Digite valor de B: ")
    try:
        b = float(b_str.strip().replace(",", "."))

        c_str = input("Digite valor de C: ")
        try:
            c = float(c_str.strip().replace(",", "."))


            # iniciando cálculo da fórmula de báskara

            # calculando delta
            baoquadrado = b ** 2
            delta = baoquadrado - (4 * a * c)
            if (delta < 0):
                print("Equação não há solução real.")
                
            else:
                    
                # calculando raíz de delta
                raizdelta = math.sqrt(delta)

                # dobro de a
                dobroA = 2 * a

                # b negativo
                bnegativo = -(b)

                # calculando x'
                x = (bnegativo + raizdelta) / dobroA
                # calculando x"
                xx = (bnegativo - raizdelta) / dobroA

                print("Resultado: \n   Valor de x' : " + str(x) + " \n   Valor de x'': " + str(xx))

            
        except:
            print("Valor de C é inválido. Abortando exercício...")
       

    except:
        print("Valor de B é inválido. Abortando exercício...")






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
