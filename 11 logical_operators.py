var1 = 3
var2 = 3
var3 = 4

# and
print(var1 == var2 and var1 == var3) #tem que ser minusculo
print(var1 == var2 and var1 == var3 and var3 == var2) #vários

# or
print(var1 == var2 or var1 == var3 and var2 == var3) # true
print((var1 == var2 or var1 == var3) and var2 == var3) # false

# prioridades not > and > or

# not
print(var1 == var2 and not var1 == var3)
