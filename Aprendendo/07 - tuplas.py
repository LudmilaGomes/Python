# TUPLAS - 7

"""

As tuplas funcionam exatamente como listas, mas elas não podem ser alteradas no local, ou seja, são imutáveis.
São escritas como uma série de objetos entre parênteses separados entre vírgulas, não entre colchetes.

Tuplas são coleções ordenadas de objetos arbitrários, acessadas pelo deslocamento, pertencem à categoria de
sequências imutáveis, têm comprimento fixo, são heterogêneas, podem ser aninhadas arbitrariamente e são arrays
de referências de objeto

tupla = (0, "spam", 3.14)

As tuplas não suportam métodos como 'append()', mas suportam operações comuns às sequências, como concatenação, repetição
indexação e fracionamento.

"""

t1 = ()         # tupla vazia

# como parênteses também podem englobar expressões, é preciso colocar esta ',' para indicar ao Python que se trata de uma tupla e não uma expressão
t1 = (40)       # um inteiro
t1 = (40,)      # tupla com um elemento

t1 = (0, 1, 2)  # tupla de 3 itens
# O Python permite a omissão dos parênteses das tuplas em contextos onde não é sintaticamente ambíguo fazer isso
t2 = 0, 1, 2    # tupla de 3 itens, como a declaração acima

t1[0]           # indexação
t1[1:2]         # fracionamento
len(t1)         # comprimento da tupla
t1 + t2         # concatenação
t2 * 3          # repetição
for x in t2:    # iteração
    print(x)
3 in t2         # participação como membro

"""

As operações de concatenação e fracionamento retornam novas tuplas, quando aplicadas às tuplas

O porquê das tuplas: elas garantem a integridade dos seus elementos e podemos ter certeza de que nenhum valor será alterado em
outra parte do programa. Não há essa garantia para as listas.

"""
