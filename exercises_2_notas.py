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


