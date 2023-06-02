# STRINGS EM PYTHON - 3

"""

String é um conjunto ordenado de caracteres.

Python não tem nenhum tipo especial para caracteres simples (como o tipo 'char' em C), apenas strings
de um só caractere.

As strings de Python são classificadas como sequências imutáveis - possuem uma ordem posicional que vai da
esquerda para a direita e não podem ser alteradas no loca. 

Strings vazias são escritas com duas aspas sem nada entre elas: 

 nome = ""

Existem várias maneiras de escrever as strings em código:

com apóstrofo, aspas, apóstrofos ou aspas triplas, sequência de escape, strings brutas e strings Unicode

"""

# podemos usar apóstrofos ou aspas, pois torna o uso dos caracteres de apóstrofo e aspas na string mais fácil (não é preciso usar seu escape: \' ou \");
s1 = 'spa"m'
s1= "spa'm"
s1 = "spa\"m"
s1 = "spa\'m"

s1 = '''spam'''
s1 = """spam"""
s1 = "a\tb\nc\am"
# s1 = r"C:\new\test.spm"   - strings brutas;
# s1 = u'eggs\u0020spam'    - strings Unicode;
s1 = "Meaning " + "of" + " Life"
print(s1)


"""

 "spa\"m"
 "spa\'m"

As barras invertidas são usadas para introduzir definições de byte especiais, conhecidas como sequências de escape.
As sequências de escape nos permitem incorporar códigos de byte em strings, que não podem ser digitados facilmente no teclado.

"""

s1 = "a\nb\tc"
print(s1)
print("Tamanho de s1: " + str(len(s1))) # a + \n + b + \t + c = 5 caracteres no total;

"""

Temos uma string bruta quando, antes de escrever a string, indicamos um 'r' na frente, como:

 r"C:\new\test.spm"

Se a letra 'r' aparece antes das aspas/apóstrofo de abertura de uma string, ela desativa o mecanismo de escape. Então, o
Python mantém suas barras invertidas literalmente, exatamente como foi digitado. Ou pode ser escrito:

"C:\\new\\test.spm"

Agora, sobre as aspas triplas usadas na declaração de strings, as aspas triplas definem strings de bloco de várias linhas.

"""

mantra = """Sempre olhe
para o lado
bom da vida."""

print(mantra)

"""

Strings em Unicode são normalmente chamadas de strings de caractere amplas. As strings em Unicode permitem que os programas
codifiquem conjuntos de caracteres mais ricos do que as strings padrão. Normalmente, as strings em Unicode são usadas para
suportar a internacionalização de aplicativos. Elas permitem que os programadores suportem diretamente conjuntos de caracteres
europeus ou asiáticos em scripts em Python.

"""

s1 = u"Fu\u00dfb\u00e4lle"  #  exemplo para mostrar a utilização da string em Unicode;
print(s1)



# ================================//================================
# STRINGS EM AÇÃO



# operações
print("\nTamanho da string 'abc': " + str(len("abc")))  # para obter o tamanho da string: len(str)
print("abc" + "def")                                    # para concatenar strings: s1 + s2
print("Ni!" * 5)                                        # para repetir a mesma string várias vezes: str * 4

"""

Formalmente, somar dois objetos string cria um novo objeto string com o conteúdo de seus operandos unidos.

"""

s1 = "Smile in the age of worry"

for x in s1:    # laço de repetição para percorrer uma string
    print(x)

myJob = "hacker"

# uso da instrução 'in' com strings
print("k" in myJob) # True
print("z" in myJob) # False

"""

Os caracteres de uma string são buscados por indexação - fornecendo o deslocamento numérico do componente desejado, entre colchetes, 
após a string. Você recebe a string de um único caractere. 

Os deslocamentos começam em zero e terminam no tamanho da string menos um.

"""

s = "spam"      # tamanho da string s: 4

#  s  p  a  m
#  0  1  2  3
#  0 -3 -2 -1
# -4 -3 -2 -1

# indexação
print(s[0])     # primeiro caractere
print(s[3])     # último caractere: 4 - 1 = 3

print(s[-1])    # primeiro caractere (da direita para a esquerda)
print(s[-2])    # segundo caractere (da direita para a esquerda)
print(s[-3])    # terceiro caractere (da direita para a esquerda)
print(s[-4])    # quarto caractere (da direita para a esquerda)

# fracionamento
print(s[1:])    # do segundo caractere até o fim
print(s[1:3])   # do segundo caractere até o fim, sem contar com esse último caractere
print(s[2:])    # do terceiro caractere até o fim
print(s[1:2])   # do segundo caractere até o terceiro, sem contar com o terceiro
print(s[:3])    # do começo até o último, sem contar com esse último caractere

print(s[-1:])   # do primeiro caractere (da direita para a esquerda) até o final (da direita)
print(s[:-1])   # do primeiro caractere (da direita para a esquerda) até o final (da esquerda), sem contar com esse primeiro caractere

# print(s[-5])  - isso não existe


# ================================//================================
# CONVERSÃO DE STRINGS

"""

Você não pode somar um número e uma string em Python, mesmo que a string pareça um número (composta de dígitos)

 '42' + 1 é errado

Como '+' pode significar adição ou concatenação, a escolha da conversão seria ambígua. Então, o Python trata isso como um erro.
Assim, é preciso empregar técnicas de conversão de string para número ou número para string:

 int('42'), str(42) - são as técnicas de conversão mais recentes

"""

print("Resultado: " + str( 49 + int("1") ) ) # a soma funciona corretamente; o 'str()' é usado para que o 'print()' não dê erro


# ================================//================================
# ALTERANDO STRINGS

"""

Como strings são sequências imutáveis, as instruções a seguir seriam incorretas:

 s1 = "spam"
 s1[0] = "x"
 
Então, para alterar uma string, é preciso construir e atribuir uma nova string, usando ferramentas como concatenação e fracionamento, e
possivelmente atribuindo o resultado de volta ao nome original da string.

Ex1:

 s1 = "spam"
 S = "Burguer"

 S = s1 + S = "spamBurguer"

Ex2:

 S = "spamSPAM!"
 S = S[:4] + "Burguer" + S[-1] = "spamBurguer!"

Pode-se usar a instrução 'sprintf()' da linguagem C para formatação:

Ex:

 "Isso é %d pássaro(s) %s(s)\n" % (1, "vivo")

"""

s1 = "spam"
S = "Burguer"

S = s1 + S
print(S)

S = "spamSPAM!"
S = S[:4] + "Burguer" + S[-1]
print(S)

print("Isso é %d pássaro(s) %s(s)\n" % (1, "vivo"))

# ================================//================================
# FORMATAÇÃO DE STRINGS

"""

O Python também utiliza o '%' para trabalhar em strings. Então, quando aplicado a strings, ele tem o mesmo uso do 'sprintf()' de C;
o operador % oferece uma maneira simples de formatar valores como strings, de acordo com uma string de definição de formato.

%d - para números inteiros
%s - para strings
%c - para caracteres
%u - para números sem sinal (inteiro) - unsigned
%f - para número de ponto flutuante - float
%% - para imprimir o caractere '%' - % literal

"""

nome = input("Digite seu nome: ")
print("Olá, %s!\n" % nome)


# ================================//================================
# MÉTODOS DE STRINGS

"""

Buscas de métodos:      objeto.método(argumentos)

Expressões de chamada:  função(argumentos)

Agora, sobre os métodos existentes no Python:

-> REPLACE:
Como as strings são imutáveis, elas não podem ser alteradas no local diretamente. Mas, usando o método 'replace()', podemos
substituir uma substring de uma string por outra substring

Ex1:

 s = "spammy"
 s = s.replace("mm", "xx") 
 % s = "spaxxy"

Ex2:
 
 "aa$bb$cc$dd".replace("$", "SPAM") 
 % "aaSPAMbbSPAMccSPAMdd"

-> FIND:
O método 'find()' retorna a posição na string onde aparece determinado caractere/substring:

Ex1:
 
 s = xxxxSPAMxxxxSPAMxxxx
 onde = s.find("SPAM") 
 % onde = 4

Se a substring não for encontrada dentro da string, o método retorna -1.

Como as strings são imutáveis, os métodos não alteram a string no local, apenas criam um novo objeto. Então, se for preciso usar 'replace()'
muitas vezes, o programa pode ser prejudicado devido o grande uso de memória. Assim, seria mais interessante passar a string para uma lista:

 s = "spammy"
 l = list(s) 
 % l = ["s", "p", "a", "m", "m", "y"]

 l[3] = "x"
 l[4] = "x"
  % l = ["s", "p", "a", "x", "x", "y"]

-> A função interna 'list()' constrói uma nova lista a partir dos itens de qualquer sequência - separando os caracteres de uma string e guardando-os
numa lista, no exemplo acima.

Assim, podemos fazer várias alterações nos caracteres, pois as listas permitem mudança dos seus elementos. Após as alterações, podemos usar
o método de string 'join()' para implodir a lista de volta em uma string:

 s = ""
 s = s.join(l)
 # s = "spaxxy"

-> Como funciona o 'join()': ele reúne as strings da lista com o delimitador entre os itens

 "SPAM".join(["eggs", "sausage", "ham", "toast"]) = 'eggsSPAMsausageSPAMhamSPAMtoast' # onde "SPAM" é o delimitador

-> Outra função comum dos métodos de string é como uma forma simples de análise de texto - analisar a estrutura e extrair uma
substring. Se os dados dentro de uma string são separados por algum tipo de delimitador, podemos usar o método de string 'spli()'.
Esse método corta uma string, transformando-a em uma lista com as substrings, em torno de um delimitador

Ex1:

 linha = "aaa bbb ccc"
 linha = linha.split()
 # linha = ["aaa", "bbb", "ccc"]

Nenhum delimitador foi indicado dentro dos parênteses, então o método split() entende que o delimitador é " " - espaço em branco.

Ex2:

 linha = "Bob, hacker, 40"
 linha = linha.spli(",")
 # linha = ["Bob", "hacker", "40"]

"""


# ================================//================================
# O MÓDULO ORIGINAL

"""

Na primeira década de existência do Python, ele fornecia um módulo de biblioteca padrão chamado 'string', com quase a totalidade das funções 
atuais presentes. A pedido dos usuários, o Python mudou e essas funções se tornaram disponíveis como métodos de objetos string. Assim, como
muitas pessoas (antes da atualização) escreviam códigos que contavam com o módulo string original, ele foi mantido por questões de compatibilidade
com as versões anteriores. Então, as seguintes formas são equivalentes:

"""

# 1ª forma
s = "a + b + c"
s = s.replace("+", "-")

# 2ª forma
import string
x = string.replace(s, "-", "SPAM")

"""

Apesar de ambos funcionarem e serem aceitos pelo Python, é mais indicado o uso dos métodos, pois com o módulo é necessário que haja a
importação dele, caracteres a mais são escritos e, além disso, o módulo pode ser executado mais lentamente do que os métodos. 

Por outro lado, algumas instruções estão só disponíveis como métodos, ou como funções do módulo. Também, alguns programadores preferem
importar o módulo, pois o nome do módulo torna mais evidente que o código utiliza funções do módulo string.

Enfim, a escolha é do programador.

"""