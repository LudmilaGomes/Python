# CATEGORIAS DE TIPO GERAIS - 4

"""

Os tipos compartilham conjuntos de operações por categoria. Então:

 - números suportam adição, subtração, multiplicação, ...
 - sequências suportam concatenação, indexação, fracionamento, ...
 - mapeamentos suportam indexação pela chava, ... (ainda não visto)

Entendemos que para todo objeto de sequência X e Y:

 - X + Y gera um novo objeto sequência com o conteúdo dos dois operandos
 - X * N gera um novo objeto sequência com N cópias do operando X na sequência

Assim, essas operações funcionam para strings, listas, tuplas, entre outros.

"""

s1 = "cuscuz com"
s2 = " carne de charque"

print(s1 + s2)  # une as duas strings

l1 = ["ovo", "pão", "queijo", "café"]
l2 = ["macarrão", "feijão", "carne", "suco"]

print(l1 + l2)  # une as duas listas

print(s1 * 6)   # imprime a string 6 vezes
print(l1 * 6)   # imprime a lista 6 vezes