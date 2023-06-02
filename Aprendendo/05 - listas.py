# LISTAS - 5

"""

As listas são muito flexíveis quando comparadas às strings (ou quando comparadas aos Arrays de C). Listas podem conter elementos de qualquer tipo,
como números, strings, até outras listas.

São coleções ordenadas de objetos arbitrários, acessadas pelo deslocamento, têm comprimento variável, podem ser heterogêneas, são
sequências mutáveis (podem ser alteradas em local). As listas lembram arrays de ponteiros.

Escritas, as listas são uma série de objetos dentro de colchetes e separados por vírgula:

 lista = [0, 1, 2, 3, 4]    # list com 5 elementos

"""


# ================================//================================
# LISTAS EM AÇÃO

lista = [0, 1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]

tamLista = len(lista)       # tamanho da lista
lista3 = lista + lista2     # concatenação de listas
print(lista * 3)            # repetição
print(3 in lista)           # participação em lista: 3 está em 'lista'? 1 - true // 0 - false
for x in lista3:            # iteração
    print(x)

"""

O operador '+' funciona como concatenação com strings e listas, mas esse operador espera o mesmo tipo de sequência dos dois lados; caso 
contrário, você receberá um erro.

"""

lista = [1, 2] + list("34") # 'list()' só funciona quando o argumento é uma string
print(lista)

# como strings, listas também funcionam com indexação e fracionamento

lista = ["spam", "Spam", "SPAM!"]

print(lista[2])         # indexação
print(lista[-2])        

print(lista[:-2])       # fracionamento


# Matrizes - array de duas dimensões

lista = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

"""

Como listas são sequências mutáveis, elas suportam alterações que realizem mudanças nos objetos em local.

Com listas, podemos alterar elementos específicos (por meio de deslocamento) ou uma seção inteira (fracionamento).

"""

# elemento específico é alterado
lista = ["spam", "Spam", "SPAM!"]
lista[0] = "ovos"
print(lista)

# seção é alterada
lista = ["spam", "Spam", "SPAM!"]
lista[0:2] = ["ovos", "comidas"]
print(lista)

"""

Com a alteração por fracionamento, não é obrigatório que a quantidade de elementos excluídos seja igual à quantidade de itens inseridos.

"""

# neste exemplo, o 2 foi excluído, mas foram inseridos o 4 e 5
lista = [1, 2, 3]
lista[1:2] = [4, 5]
print(lista)

# exclusão de elemento - o 2 é excluído
lista = [1, 2, 3]
lista[1:2] = []
print(lista)


# Métodos de lista

"""

 -> APPEND
Esse método simplesmente um item no final da lista. Ao contrário da concatenação, 'append()' espera que você passe um único elemento, não 
uma lista.

 -> SORT
Esse método ordena os elementos da lista em ordem crescente (também funciona com strings).

Esses dois métodos alteram o objeto da lista associado no local, mas não retornam a lista como resultado, então:

l = l.append(x)     - está errado, e todos os elementos da lista serão perdidos, pois 'append()' retorna 'None'.

 -> EXTEND
Adiciona vários elementos à lista.

 -> POP
Exclui o último item da lista e retorna esse valor.

 -> REVERSE
Inverte a lista no local.

 -> DEL
Pode ser usada para excluir um elemento da lista ou uma seção inteira.

"""

lista = [7, 3, 1, 9]

lista.append(5)         
print(lista)

lista.sort()            
print(lista)

lista.extend([2, 8, 4]) 
print(lista)

print(lista.pop())
print(lista)

lista.reverse()
print(lista)

lista = ["comida", "cuscuz", "pizza", "macarrão"]
del lista[0]
print(lista)
del lista[1:]
print(lista)

