var1 = 3
var2 = 7


# condicao simples
if var1 > var2:
    print("var 1 é maior")

if var2 > var1:
    print("var 2 é maior")

# condicao com senão
if var1 > var2:
    print("var 1 é maior")
else:
    print("var 2 é maior")


var3 = -1
var4 = 0

# condicao aninhadas
if var3 < var4:
    if var3 < 0:
        print("var3 é menor que var4\nvar3 é menor que zero")
    else:
        print("var3 é menor que var4\nvar3 é maior que zero")
else:
    print("var4 é maior que var3")


var5 = 0
var6 = 0

# condicao senão-if
if var5 > var6:
    print("var 5 é maior")
elif var5 < var6:
    print("var 6 é maior")
else:
    print("var 5 e var 6 são iguais")
