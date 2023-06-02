# INSTRUÇÕES DE ATRIBUIÇÃO, EXPRESSÕES E IMPRESSÃO - 12

"""

INSTRUÇÕES DE ATRIBUIÇÃO

Já usamos essa instrução para atribuir objetos a nomes. Em sua forma
básica, você escreve um 'destino' de uma atribuição à esquerda de um
sinal de igualdade e um 'objeto' a ser atribuído, à direita. O destino 
à esquerda pode ser um nome ou componente de objeto e o objeto à direita
pode ser uma expressão arbitrária que calcula um objeto.

As atribuições criam referências de objeto: as atribuições do Python
armazenam referências para objetos em nomes ou estruturas de dados. Por
isso, as variáveis de Python são muito mais parecidas com ponteiros do
que com áreas de armazenamento de dados.

Os nomes são criados ao serem atribuídos pela primeira vez, então não
há necessidade de declarar nomes previamente (como em C, em que antes
declarávamos a variável e depois atribuíamos um valor para ela; no caso
em Python, isso não é necessário).

Os nomes devem ser atribuídos antes de serem referenciados. Assim, é um
erro usar um nome para o qual você ainda não atribuiu um valor.

Atribuições implícitas: neste momento, a preocupação maior é com a
instrução '=', mas a atribuição ocorre em muitos outros contextos em
Python. Como nos exemplos abaixo:

 Spam, ham = 'yum', 'YUM'       - atribuição de desempacotamento de tupla
 [spam, ham] = ['yum', 'YUM']   - atribuição de desempacotamento de lista
 spam = ham = 'lunch'           - destino múltiplo

"""

# abaixo, mesmo com essas atribuições diferentes, criamos apenas nomes que referenciam um valor string
# ou seja, 'Spam' e 'ham' são simplesmente variáveis comuns

Spam, ham = 'yum', 'YUM'
print(Spam)
print(ham)
[Spam, ham] = ['yum2', 'YUM2']
print(Spam)
print(ham)
# 'Spam' e 'ham' recebem uma referência para o mesmo objeto string 'lunch'
Spam = ham = 'lunch'
print(Spam)
print(ham)

"""

REGRAS DE NOME DE VARIÁVEL

Sintaxe: (sublinhado ou letra) + (qualquer números de letras, algarismos ou sublinhados).
Os nomes de variável devem começar com um sublinhado OU com uma letra,
seguido de qualquer números de letras, algarismos ou sublinhados.

exemplos de nomes válidos: '_spam', 'spam' e 'Spam_1'
exemplos de nomes INválidos: '1_Spam', 'spam$' e '%$#!'

Maiúsculo importa: 'SPAM' não é o mesmo que 'spam'.
O Python sempre presta atenção a maiúsculos nos programas, tanto em 
nomes criados, quanto em palavras reservadas da linguagem. Então,
'X' e 'x' são variáveis diferentes, por exemplo.

As palavras reservadas estão fora dos limites:
Os nomes que definimos não podem ser iguais às palavras que têm
significado especial na linguagem Python. Se tentarmos usar a palavra
'class', o Python acusará um erro de sintaxe, mas 'klass' e 'Class'
funcionam bem.

Além dessas regras, existem também convenções de atribuição de nomes,
regras não obrigatórias, mas que são usadas na prática:

 - nomes que começam com um único sublinhado ('_x') não são importados
   por uma instrução 'from module import';
 - os nomes que têm dois sublinhados no início e no fim ('__x__') são
   nomes definidos pelo sistema, os quais têm significado especial para
   o interpretador;
 - nomes que começam com dois sublinhados ('__x') são localizados nas
   classes que os englobam;
 - o nome que é apenas um sublinhado ('_') mantém o resultado da última
   expressão, ao se trabalhar interativamente.

Também existem convenções que existem entre os programadores. Por exemplo,
nomes de classes começam com a primeira letra maiúscula.

"""

# ======================//======================

"""

Importante lembrar: os nomes não têm tipo, mas os objetos têm.

É necessário manter clara a distinção do Python entre nomes e objetos.
Os objetos têm um tipo e podem ser mutáveis ou não. Por outro lado, os
nomes são sempre apenas referências para objetos. Os nomes não têm
nenhuma noção de mutabilidade e nenhuma informação de tipo associada,
fora o tipo do objeto que referenciam em dado momento.

 x = 0          # x é vinculado a um objeto inteiro;
 x = 'Olar'     # agora, vinculado a uma string;
 x = [1, 2, 3]  # e, agora, a uma lista;

"""

# ======================//======================

"""

Instruções de atribuição ampliadas:
A partir do Python 2.0, está disponível um conjunto de formatos de
instrução de atribuição adicionais. Emprestados da linguagem C, esses
formatos são apenas atalhos

 x = x + y  # forma tradicional
 x += y     # atalho

Esse formato também serve para os outros símbolos de operações do Python.

 x = x + 1
 x += 1

Quando aplicado a uma string:

 s = 'spam'
 s = s + 'SPAM' # forma tradicional
 s += 'SPAM'    # atalho

Quando aplicado a uma lista:

 l = [1, 2]     # concatenação: forma mais lenta
 l = l + [3]    # ou l += [3]
 print(l)       # l = [1, 2, 3]
 
 l.append(4)    # forma mais rápida, mas no local
 print(l)       # l = [1, 2, 3, 4]

Para um conjunto de itens na lista:

 l = l + [5, 6] # concatenação: forma mais lenta; ou l += [5, 6]
 print(l)       # l = [1, 2, 3, 4, 5, 6]

 l.extend([7, 8])   # forma mais rápida, mas no local
 print(l)           # l = [1, 2, 3, 4, 5, 6, 7, 8]

Em todos os casos, a concatenação será mais lenta (processo menos 'otimizado'),
mas é o procedimento menos propenso aos efeitos colaterais das referências
compartilhadas, já que a concatenação precisa criar um novo objeto, copiar
na lista da esquerda e depois copiar na lista da direita. Em contraste,
as chamadas de método no local simplesmente adicionam itens no final de
um bloco de memória.

"""

# ======================//======================

"""

INSTRUÇÕES DE EXPRESSÃO

Expressões também podem ser utlizadas como instruções. Mas isso sõ faz
sentido essa expressão fizer algo útil como efeito colateral. Usamos
expressões em duas situações:

Para chamadas de funções e métodos e para imprimir valores, já que o 
Python irá imprimir o resultado da expressão digitada.

 spam(eggs, ham)            # chamada de função
 spam.ham(eggs)             # chamada de método
 spam                       # impressão
 spam < ham and ham != eggs # expressões compostas
 spam < ham < eggs          # teste de intervalo

Sobre o último exemplo: o Python nos permite enfileirar teste de comparação
de grandeza para escrever comparações encadeadas. Por exemplo, a expressão
(A < B < C) testa se B está entre A e C; isto é equivalente ao teste
booleano (A < B and B < C), mas é mais fácil de ler e digitar.

"""

# ======================//======================

"""

INSTRUÇÕES DE IMPRESSÃO

a instrução 'print()' simplesmente imprime objetos. Vimos métodos de arquivo
que gravam texto. A instrução print é semelhante, mas é mais focalizada:
print grava objetos no fluxo de stdout (com alguma formatação padrão),
mas os métodos de gravação de arquivo gravam strings em arquivos. Então,
como o fluxo de saída padrão está disponível no Python, no módulo interno
sys é possível simular a instrução print com gravações de arquivo, mas
print é mais fácil de usar.

"""

print("spam, ham", end = "")  # imprime objeto em sys.stdout; indica para terminar sem '\n'
print("spam, ham")            # imprime objeto em sys.stdout; adiciona '\n' no final

x = "a"
y = "b"

print(x + y)
print(x + " ... " + y)
print("%s ... %s" % (x, y))

# imprimindo da maneira difícil
import sys

sys.stdout.write("Olá, mundo\n")

# então:

print(x)
# é equivalente a
sys.stdout.write(str(x) + '\n')