# LOOP WHILE

import os

os.system('cls')

"""

while ( enquanto isto for verdadeiro )
    instruções

"""

i = 0

while(i < 9):
    print("Valor de i: " + str(i))
    i+=1
    if i == 5:
        break

# =================//=================

comidas = ["cuscuz", "farinha de mandioca", "ameixa", "salada mista", "farofa"]

i = 0
tam = len(comidas)

while(i < tam):
    print(comidas[i])
    i+=1

# =================//=================

nome = input("Digite um novo nome: ")
nomes = []

while (nome != "-1"):

    nomes.append(nome)
    nome = input("Digite um novo nome: ")

for x in nomes:
    print(x)

