import random

i = 10
f = 3.14
c = 5+6j

#print("Valor: " + str(i) + " e Tipo: " + str(type(i)))
#print("Valor: " + str(f) + " e Tipo: " + str(type(f)))
#print("Valor: " + str(c) + " e Tipo: " + str(type(c)))

x = int(f)
print("Valor: " + str(x) + " e Tipo: " + str(type(x)))

x = float(i)
print("Valor: " + str(x) + " e Tipo: " + str(type(x)))

r = random.randrange(0, 100)

print(r)

r = [
    random.randrange(0, 100), 
    random.randrange(0, 100), 
    random.randrange(0, 100), 
]

print(r)