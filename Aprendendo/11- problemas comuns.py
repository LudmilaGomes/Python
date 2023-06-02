# PROBLEMAS DOS TIPOS INTERNOS  - 11

"""

A atribuição cria referências e não cópias:

Em Python, precisamor entender o que está acontecendo com as referências compartilhadas
no programa.

Se não queremos referências compartilhadas, temos de copiar explicitamente os objetos.

"""

from copy import copy

l = [1, 2, 3]
m = l

print(m)
l[0] = 49
print(m)    # também altera 'm'

# ======================//======================
# para evitar referência compartilhada:

l = [1, 2, 3]

m = l[:]
# ou
m = list(l)
# ou
m = copy(l)
# e 'm' e 'l' terão alterações independentes em seus valores, por assim dizer

"""

Problemas de referências Versus cópias com a operação de repetição:

A operação de repetição cria cópias, mas quando sequências mutáveis são aninhadas, o efeito
pode nem sempre ser como o esperado.

No exemplo abaixo, como 'l' foi aninhada na seguinda repetição, 'y' acaba incorporando referências
para a lista original atribuída a 'l'. Então, se alterarmos um valor de 'l', valores em 'y' também 
serão alterados.

Então, é preciso estar atento aos casos em que a concatenação, repetição e fracionamento realizam 
cópias.

"""

l = [4, 5, 6]
x = l * 4   # 'x' recebe quatro cópias de 'l'
y = [l] * 4 # 'y' recebe 4 listas de 'l'

print(x)
print(y)

l[0] = 34
print(x)    # 'x' não sofre alteração pois a repetição realiza cópias
print(y)    # 'y' sofre alteração

# ======================//======================
# para evitar referência compartilhada na sequência aninhada:

l = [4, 5, 6]

x = l * 4   # 'x' recebe quatro cópias de 'l'
y = list(l) * 4 # 'y' recebe 4 listas de 'l'

print(x)
print(y)

l[0] = 34
print(x)    # 'x' não sofre alteração pois a repetição realiza cópias
print(y)    # 'y' não sofre alteração

"""

Estruturas de dados cíclicas:

Se um objeto coleção contém uma referência para ele mesmo, chamamos ele de objeto cíclico.
O Python imprime "[...]" quando detecta um ciclo no objeto. 

Esse tipo de caso (em que aparece um ciclo no objeto) pode levar a problemas, se não forem
antecipados.

Na dúvida, prefira não usar referência cíclica, a não ser que saiba tratar deles.

"""

l = ["cuscuz"]
l.append(l)
print(l)    # imprime: ['cuscuz', [...]]

"""

Os tipos imutáveis não podem ser alterados no local:

Não podemos alterar um objeto imutável no local.

Para realizar alterações, construa um novo objeto com fracionamento, concatenação, etc.., e 
atribua-o de volta à referência original.

"""

t = (1, 2, 3)
# t[2] = 4          - isso é um erro! Mas...
t = t[:2] + (4,)    # ... isso pode ser feito
print(t)            # imprime: (1, 2, 4)