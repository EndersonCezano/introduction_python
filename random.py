import random

num = random.randint(5, 15)
print(num)

lista = [54, 58, 47, 21, 84, 62]
num2 = random.choice(lista)
print(num2)

random.seed(2)
num = random.randint(5, 15)
print(num)
