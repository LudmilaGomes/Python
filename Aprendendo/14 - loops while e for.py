# WHILE E FOR - 14

"""

O loop while fornece uma maneira de desenvolver loops gerais. O loop
for foi projetado, por sua vez, para percorrer os itens de um objeto
de sequência e executar um bloco de código para cada item.

WHILE:

Executa repetidamente um bloco de instruções indentadas, contanto que
um teste no início continue avaliando um valor verdadeiro. Quando o
teste se torna falso. Quando o teste se torna falso, o controle continua
após todas as instruções presentes no bloco; as instruções de dentro
do while não são executadas se o teste é falso desde o início.

 while <teste>:     # faz um loop em teste
     <instruções1>  # miolo do loop
 else:              # else opcional
     <instruções2>  # executadas se não saiu do loop com break

"""

# exemplo 1

x = "comer pizza"
# fraciona o primeiro caractere de uma string, até que a string esteja vazia (falso)
while x:
    print(x)
    x = x[1:]   # retira o primeiro caractere de x

print()

# exemplo 2

i = 0
# conta do valor 0 até (mas não incluindo) 10
while i < 10:
    print(i)
    i += 1


# ======================//======================

"""

Instruções 'break', 'continue', 'pass' e cláusula else:

 - break: 
sai do loop mais próximo que a envolve.
 - continue: 
pula para o início do loop mais próximo que a envolve.
 - pass: 
não faz nada ;-;
 - bloco else do loop: 
é executado se, e somente se, saímos do loop
normalmente - sem atingir uma instrução break.

 while <teste1>:
     <instruções1>
     if <teste2>: break     # sai do loop agora, pula a cláusula else
     if <teste3>: continue  # vai para o início do loop agora
 else:
     <instruções2>          # se não atingirmos uma instrução 'break'


A instrução 'pass' é usada quando a sintaxe exige uma instrução mas
você não tem nada de útil a fazer. Ela é usada para escrever um miolo
vazio de uma instrução composta.

 while 1: pass

Como o miolo é apenas uma instrução vazia, o Python fica preso nesse
loop. De forma aproximada, o pass está para as instruções assim como
None está para os objetos - um nada explícito.

A instrução 'continue' é um salto imediato para o início de um loop.

 x = 10
 while x:
     x -= 1
     if x % 2 != 0: continue  # ímpar: pula
     print(x)

A instrução 'break' é uma saída imediata do loop.

"""

# o loop continua enquanto o nome recebido for diferente de '0'

while 1:
    nome = input("Digite seu nome: ")
    if nome == "0": break
    idade = int(input("Digite sua idade: "))
    print("Olá, %s => idade %d" % (nome, idade))


# ======================//======================


"""

A cláusula else será executada se o miolo do loop nunca for executado.
No while, isso acontece se o teste no cabeçalho é falso logo no início.

"""

# ======================//======================

"""

O loop for pode percorrer itens de qualquer objeto sequência ordenada.
Então, o for funciona com listas, strings, tuplas e com novos objetos.

O for começa com uma linha de cabeçalho que especifica um destino de
atribuição, junto com um objeto que você queira percorrer. Assim, a 
variável 'destino' assumirá os valores que estão nas posições do ob-
jeto de sequência ordenada 'objeto'.

 for <destino> in <objeto>:
     <instruções1>
 else:
     <instruções2>

Quando o Python executa um loop for, ele atribui os itens do objeto
sequência ao destino, um por um, e executa o miolo do loop para cada
um.

"""

# exemplo 1 - exibe todos os elementos da lista
for x in ["macarrão", "arroz", "feijão", "farinha"]:
    print(x)

# exemplo 2 - calcula a soma dos itens da lista
soma = 0
for x in [1, 2, 3, 4]:
    soma += x
print(soma)

# exemplo 3
s, t = "é sobre isso, ", ("e", "tá", "tudo", "bem")
for x in s:
    print(x, end="")
for x in t:
    print(x, end=" ")

print()

# exemplo 4
t = [(1, 2), (3, 4), (5, 6)]
# é como atribuir em cada passagem pelo loop: (a, b) = (1, 2)
for (a, b) in t:
    print(a, b)

# exemplo 5
itens = ["aaa", 111, (4, 5), 3.14]
testes = [(4, 5), 3.14]

for chave in testes:
    for valor in itens:
        if chave == valor:
            print(str(chave) + " foi encontrado")
            break
    else:
        print(str(chave) + " não foi encontrado")


# exemplo 6
for x in [1, 2, 3, 4, 5]:
    for y in [3, 4, 5, 6, 7]:
        print("X: " + str(x) + " e Y: " + str(y))
        if x == y:
            print("x e y são iguais.")
            break
    else:
        print("x e y não são iguais.")

# exemplo 7
seq1 = "spam"
seq2 = "scam"
resultado = []
for x in seq1:
    if x in seq2:
        resultado.append(x)
print(resultado)


# ======================//======================

"""

FOR

O loop for subordina a maioria dos loops estilo contador. Geralmente,
ele é mais simples de escrever e mais rápido para executar do que um
loop while, de modo que é a primeira ferramenta que você deve buscar
quando precisar percorrer uma sequência. Mas, existem casos em que
você vai precisar iterar de uma maneira mais especializada.

Essas iterações exclusivas podem ser feitas com um loop while e com
indexação manual, mas o Python fornece duas funções internar que te
permitem especializar iterações em um loop for:

 - a função interna 'range' retorna uma lista de inteiros sucessivamente
 mais altos, que podem ser usados como índices em um loop for;
 - a função interna zip retorna uma lista de tuplas de itens paralelos,
 que podem ser usadas para percorrer várias sequências em um loop for.

A função range:
Com um argumento, range gera uma lista com inteiros de zero até (mas
não incluindo) o valor do argumento. Se você passar dois argumentos,
o primeiro será considerado como o limite inferior. Um terceiro argumento
opcional pode fornecer um "passo"; se for usado, o Python soma o passo
a cada inteiro sucessivo no resultado (o padrão dos passos é um). Os
intervalos também podem negativos ou em ordem decrescente.

 range(5), range(2, 5), range(0, 10, 2)
 [0, 1, 2 , 3, 4], [2, 3, 4], [0, 2, 4, 6, 8]

 range(-5, 5)
 [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

 range(5, -5, -1)
 [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

Se você colocar 'range(5, -5)', iss não funciona, já que o passo padrão
é 1, e nunca alcançaremos -5 se somarmos 1 ao 5.

"""

# exemplo 1 - se não transformamos o range em list, essa exibição não funciona
lista = list(range(-5, 5))
print(lista)

# exemplo 2
lista = list(range(5, -5, -1))
print(lista)

# exemplo 3 - uma lista de deslocamentos em x é percorrido, não os itens reais de x
x = "spam"
for i in range(len(x)):
    print(x[i])

# exemplo 4
s = "abcdefghijk"
for i in range(0, len(s), 2): print(s[i])
for x in s[::2]: print(x)   # efeito semelhante ao for de cima

# exemplo 5
l =[1, 2, 3, 4, 5]
for i in range(len(l)):
    l[i] += 1   # soma um a cada item em l
print(l)

"""

Usar a função range faz percorrermos sequências com um loop for de
forma exaustiva. A função interna 'zip' nor permite usar loops for
para visitar várias sequências em parelelo. 

"""

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

print(list(zip(l1, l2)))

for (x, y) in zip(l1, l2):
    print(str(x) + " " + str(y) + " -- " + str(x + y))

"""

A função zip aceita qualquer tipo de sequência e mais de dois argumentos.

"""

# com tuplas
t1, t2, t3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
zip(t1, t2, t3)
print( list(zip(t1, t2, t3)) )

# com strings
s1 = "abc"
s2 = "xyz123"
# zip trunca as tuplas resultantes no comprimento da sequência mais curta,
# quando os comprimentos dos argumentos diferem
print(list(zip(s1, s2)))

"""

A função interna 'map' cria pares de itens de sequências de maneira
semelhante, mas preenche as sequências mais curtas com 'None', caso
os comprimentos dos argumentos sejam diferentes.

"""

print(list(map(None, s1, s2)))

"""

Normalmente, a função map recebe uma função, um ou mais argumentos
de sequência e reúne os resultados da chamada da função com itens
parelelos extraídos das sequências. Quando o argumento da função é
None, ela simplesmente cria pares de itens, como a função zip.

Além disso, podemos usar a função zip para ir de uma lista para um
dicionário:

"""

chaves = ["macarrão", "feijão", "arroz"]
valores = [1, 1, 1]
print(list(zip(chaves, valores)))

dicionario = {}
for (c, v) in zip(chaves, valores):
    dicionario[c] = v
print(dicionario)

# ou, simplesmente:

dicionario = dict(zip(chaves, valores))
print(dicionario)

"""

O nome interno 'dict' é um nome de tipo no Python. Às vezes, chamá-lo
é como uma conversão de lista para dicionário, mas na verdade é um
pedido de construção de objeto

"""