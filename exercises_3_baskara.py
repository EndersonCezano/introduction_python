
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




