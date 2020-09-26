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
