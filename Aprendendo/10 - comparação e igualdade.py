# COMPARAÇÕES, IGUALDADES E VERDADE - 10

"""

Listas equivalentes são atribuídas a l1 e l2, mas são atribuídos objetos distintos. Assim, existem duas maneiras de se testar a 
igualdade no Python:

 - o operador '==' testa a equivalência de valor;
 - o operador 'is' testa a identidade do objeto;

"""

l1 = [1, ('a', 3)]
l2 = [1, ('a', 3)]

print(l1 == l2) # retorna True - valores equivalentes
print(l1 is l2) # retorna False - objetos diferentes (duas partes diferentes da memória)

"""

No exemplo abaixo, deveríamos ter dois objetos distintos, mas com o mesmo valor. Então, '==' retorna True e 'is' deveria ser False...
A operação 's1 is s2' retorna True, pois internamente o Python reutiliza strings (como uma questão de otimização), então na
verdade só existe um objeto 'spam!' na memória, compartilhada por s1 e s2. 

"""

s1 = "spam!"
s2 = "spam!"

print(s1 == s2) # retorna True - valores equivalentes
print(s1 is s2) # retorna True - objetos iguais (mesma parte da memória)

"""

As noções de verdadeiro e falso são propriedades intrínsecas de todo objeto em Python - cada objeto é verdadeiro ou falso:

 - os números são verdadeiros, se forem diferentes de 0;
 - os outros objetos são verdadeiros, se não estiverem vazios;

O Python fornece também um objeto especial chamado 'None', que também é considerado falso; é muito parecido com o ponteiro
NULL de C.

Por exemplo, nas listas, você não pode atribuir a um deslocamento, a não ser que ele já exista (a lista não aumenta se você
fizer uma atribuição fora dos limites - fora do tamanho atual da lista). Para alocar previamente uma lista de 100 itens, para
que possa adicionar a qualquer um dos 100 deslocamentos, você pode preencher uma lista com objetos None:

 l = [None] * 100
 print(l)  
 # len(l) = 100

"""

