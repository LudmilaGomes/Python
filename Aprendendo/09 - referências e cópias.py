# REFERÊNCIAS Versus CÓPIAS - 9

from copy import copy

lista1 = [1, 2, 3]
lista2 = lista1

lista1[0] = 0   # a lista2 também será alterada
print(lista1)
print(lista2)
print()

# =======================//=======================

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

lista1[0] = 0   # a lista2 não será alterada
print(lista1)
print(lista2)
print()

# =======================//=======================

"""

A lista1 referencia um objeto. Quando alteramos este objeto, o valor na lista2 também muda, por causa desta instrução:

lista2 = lista1

Então, a lista2 referencia o mesmo objeto que a lista1. Mas, se a intenção for não referenciar o mesmo objeto, mas sim copiar o objeto
da lista1 na lista2, o que fazer?

É necessário solicitar que seja feita a cópia do objeto com:

 - expressões de fracionamento com limites vazios copiam sequências
 - o método de dicionário 'copy()' copia um dicionário
 - algumas funções internas, como 'list()', também realizam cópias
 - o módulo de biblioteca padrão 'copy' também faz cópias completas

"""

# se temos uma lista e um dicionário com valores que não queremos que sejam alterados por outras listas ou dicionários
lista = [1, 2, 3]
dicionario = {"nome" : "Ludmila", "idade" : 18}

a = lista[:]            # em vez de 'a = lista'
a = list(lista)         # também copia os valores
b = dicionario.copy()   # em vez de 'b = dicionario'
b = copy(dicionario)    # também copia os valores

# assim, quando alteramos um valor em 'a' ou em 'b'...
a[0] = 54
b["nome"] = "ainda é Ludmila"

# ... os valores de 'lista' e de 'dicionario' permanecem inalterados
print(lista)
print(dicionario)
print()

# apenas os valores em 'a' e 'b' foram alterados
print(a)
print(b)