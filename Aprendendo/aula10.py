# IF - desvio condicional (aulas 10 e 11)

var = 0

if var > 1:
    print(str(var) + " é maior que 1")
elif var == 1:
    print(str(var) + " é igual a 1")
else:
    print(str(var) + " é menor que 1")

# =============================//=============================

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
var = input("Digite uma operação matemática: ")

if var == "+":
    res = a + b
    print("Resultado: " + str(res))
elif var == "-":
    res = a - b
    print("Resultado: " + str(res))
elif var == "*":
    res = a * b
    print("Resultado: " + str(res))
elif var == "/":
    res = a / b
    print("Resultado: " + str(res))
else:
    print("Nenhuma operação correponde a " + var)

# =============================//=============================

clima = "sol"
dinheiro = 50
lugar = ""

if clima == "sol" and dinheiro >= 100:
    lugar = "praia"
else:
    lugar = "ficar em casa"

print(lugar)