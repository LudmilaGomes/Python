# NÚMEROS - 1

"""

Python suporta os seguintes tipos de números:

números inteiros, ponto flutuante e, como C, Python permite a escrita usando literais de hexadecimal e octal.
Além desses, Python suporta a escrita de números complexos, assim como um inteiro longo com precisão ilimitada (ou quase).

"""

# INTEIRO
# Em Python 2, existiam os tipos diferentes 'int' e 'long int'. No Python 3, há apenas o 'int', mas o valor de um número inteiro
# não é restrito pelo números de bits e pode se expandir até o limite da memória disponível.
inteiro = 12
intLongo = 999999999999999999999999999999999999999999999999999

# PONTO FLUTUANTE
pontoF = 3.14
pontoF = 6e6    # 6e6 = 6 * 10^6 = 6000000

# OCTAL E HEXADECIMAL
octal = 0o177
octal = 0O177
hexadecimal = 0x12f
hexadecimal = 0X12f

# COMPLEXO
complexo = 3 + 8j
complexo = complex(3, 8) # primeiro é a parte real, depois, a imaginária do número complexo (usando a função 'complex()').
#'complexo.real' e 'complexo.imag' esta é a maneira de extrair suas partes como atributos

"""

Python possui a biblioteca NumPy (Numeric Python), que fornece ferramentas de programação numérica acançadas.

Agora, sobre operadores de expressões:
são usados os clássicos +, -, *, / para soma, subtração, multiplicação e divisão, mas há outros:

 % para calcular o resto de uma divisão;
 << para realizar um deslocamento para a esquerda em nível de bit;
 // para divisão, mas sempre trunca os restos fracionários;
 ** para potenciação. Ex.: 4 ** 2 = 4^2 = 4 * 4 = 16
 & para calcular o resultado de uma operação lógica; entre outros.

Sobre precedência de operadores:
Pode-se utilizar parênteses nas expressões escritas. Assim, o programa sempre irá avalisar as expressões dentro dos parênteses primeiro.
Quando não há parênteses, o Python executa as operações de acordo com a precedência dos utilizados operadores.

Operações em nível de bit:

>>> x = 1       # 0001
>>> x << 2      # desloca o valor 1 em 2 bits para a esquerda: 0100
 4
>>> x | 2       # função lógica OU em nível de bit: 0001 (1) ou 0010 (2) que é como uma soma: 0001 + 0010 = 0011
 3
>>> x & 1       # função lógica E em nível de bit: 0001 (1) e 0001 (1)
 1

O Python também fornece funções e módulos internos para processamento numérico.

"""

import math # importa o módulo interno 'math'

print(math.pi, math.e)

# 'math.sin()' é a função seno, do módulo 'math'
# 'abs()' é a função de Python para obter o módulo de um número
# 'pow(base, potência)' é a função para potenciação: 4 ** 2 = pow(4, 2) = 16