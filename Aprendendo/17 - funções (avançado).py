"""

Funções anônimas: Lambda

Além de 'def', o Python também fornece uma expressão que gera objetos 
função, chamada 'lambda'. Assim como a expressão 'def', ela cria uma 
função para ser chamada posteriormente, mas a retorna em vez de atribuir 
um nome a ela. Por não terem nome, são conhecidas como funções anônimas. 
Na prática, elas são usadas como uma maneira de colocar uma definição de
função em linha ou adiar a execução de um trecho de código.

A forma geral de 'lambda' é a palavra-chave lambda, seguida de um ou 
mais argumentos seguidos de uma expressão após os dois-pontos:

    lambda argumento1, argumento2,... argumentoN: expressão usando os argumentos

Os objetos função retornados pela execução de expressões lambda funcionam
de maneira igual àqueles criados e atribuídos pela instrução def. Mas a
expressão lambda tem algumas diferenças que a tornam útil em tarefas
especializadas.

'lambda' é uma expressão e não uma instrução. Por isso lambda pode apareceer
em lugares em que a instrução def não é permiida pela sintaxe do Python.

O miolo de 'lambda' é uma única expressão e não um bloco de instruções.
Lambda é projetada para desenvolver funções mais simples e def trata de
tarefas maiores.

Fora essas distinções, def e lambda fazem o mesmo tipo de trabalho:

    def func(x, y, z): return x + y + z
    >>> func(2, 3, 4) = 9

    f = lambda x, y, z: x + y + z
    >>> f(2, 3, 4) = 9

    def knights():
        title = 'Sir'
        action = (lambda x: title + ' ' + x)
        return action

As expressões lambda são opcionais, você pode usar def se quiser, mas as
lambda tendem a ser uma construção de codificação mais simples nos cenários
em que você precisa apenas incorporar pequenos trechos de código executável.



"""

