# ESCOPOS E ARGUMENTOS - 16

"""

Regras de escopo

Quando usamos um nome em um programa, o Python o cria, altera ou pesquisa
no que é conhecido como espaço de nome - um lugar onde os nomes ficam.
Quando falamos sobre a busca de um valor de um nome em relação ao código,
o termo escopo refere-se a um espaço de nome - a localização da atribuição
de um nome em seu código determina o escopo da visibilidade do nome do código.

Tudo que está relaciona aos nomes acontece em atribuições no Python - até
a classificação do escopo. Os nomes no Python começam a existir quando
recebem um valor pela primeira vez, e eles devem ser atribuídos antes
de serem usados. Como os nomes não são declarados antecipadamente, o Python
utiliza o local da atribuição de um nome para associá-lo (vinculá-lo) a um
espaço de nome em particular. Ou seja, o lugar onde você atribui um nome
determina o espaço de nome em que ele ficar e, portanto, seu escopo de
visibilidade.

Por padrão, todos os nomes atribuídos dentro de uma função são associados
ao espali de nome dessa função e a nenhum outro.

 - Os nomes definidos dentro de uma instrução def só podem ser vistos pelo
 código que está dentro dessa instrução. Então, você não pode referir-se
 a esses nomes fora da função;

 - Os nomes definidos dentro de uma instrução def não entram em conflito
 com as variáveis fora dessa instrução, mesmo que um nome igual seja usado
 em qualquer outro lugar. Um nome X atribuído fora de uma instrução def é
 uma variável completamente diferente de um nome X atribuído dentro dessa
 instrução.

Assim, os escopos de função ajudam a evitar conflitos de nomes em seus
programas e ajudam a transformar as funções em unidades de programa mais
auto-suficiente.

As funções fornecem um escopo que torna locais os nomes utilizados, de
modo que os nomes dentro de uma função não entram em conflito com os que
estão fora (em um módulo ou em outra função). As funções definem um escopo
local e os módulos (módulo - tudo aquilo que não está aninhado em uma instrução
def) definem um escopo global. Os dois escopos estão relacionados assim:

 - O módulo envolvente é um escopo global: cada módulo é um escopo global - um
 espaço de nome onde ficam as variáveis criadas no nível superior de um
 arquivo de módulo.

 - O escopo global abrange apenas um arquivo

 - Cada chamada para uma função é um novo escopo local: sempre que chama
 uma função, você cria um novo escopo local - um espaço de nome onde normalmente
 ficam os nomes criados dentro de uma função.

 - Os nomes atribuídos são locais, a não ser que sejam declarados como globais:
 por padrão, todos os nomes atribuídos dentro de uma definição de função são
 colocados no escopo local.

Parece confuso, mas podemos resumir isso em três regras simples:

 - as referências de nome pesquisam no máximo quatro escopos: local, em
 seguida as funções envolventes (se houver), depois global e, então, interno;

 - as atribuições de nome criam ou alteram nomes locais, por padrão;

 - as declarações globais fazem o mapeamente dos nomes atribuídos para o
 escopo de um módulo envolvente.

Assim, todos os nomes atribuídos dentro de uma instrução de função def
são locais por padrão; as funções podem usar os nomes em funções envolventes
e no escopo global, mas devem declarar como globais para alterá-los.

Regra LEGB:

 - quando você usa um nome não qualificado dentro de uma função, o Python
 pesquisa para cima em quatro escopos - o local (L), depois o escopo local
 de qualquer função envolvente (E), em seguida o global (G) e, então, o
 interno (B, de 'built-in').

"""

# ======================//======================

"""

Exemplos de escopo:

"""

# escopo global
x = 99

def func(y):
    # escopo local
    z = y + x
    return z

print("Resultado de 'func': " + str(func(1)))

"""

nomes globais: x e func
x é global porque foi atribuído no nível superior do arquivo de módulo;
ele pode ser referenciado dentro da função sem ser declarado como global.

nomes locais: y e z
y e z são locais para a função (e só existem quando a função é executada),
pois recebem um valor na definição da função; z, em virtude da instrução =,
e y porque os argumentos são sempre passados por atribuição.

"""

# ======================//======================

"""

Escopo interno é na verdade apenas um módulo da biblioteca padrão previamente
construído, chamado '__builtin__'.

Os nomes dessa lista são o escopo interno do Python

"""

# ======================//======================

x = 88      # x global

def func(): 
    x = 2   # x local: oculta o global

func()
print("Valor de x: " + str(x))
# imprime 88; mesmo chamando a função, x permanece inalterado

"""

Acima, a atribuição dentro da função cria um x local que é uma variável
diferente do x global no módulo fora da função. Por isso não há nenhuma maneira
de alterar um nome fora da função, sem adicionar uma declaração global na
instrução def.

"""

# ======================//======================

"""

A instrução global

É uma declaração de espaço de nome. Ela informa ao Python que uma função
pretende alterar nomes globais - nomes que ficam no escopo do módulo envolvente.

"""

x = 88      # x global

def func(): 
    global x
    x = 2   # x global

func()
print("Valor de x: " + str(x))
# imprime 2

"""

No exemplo acima, o x de dentro da instrução de agora refere-se ao x que
está fora desta instrução; desta vez, eles são a mesma variável.

"""

y, z = 1, 2         # variáveis globais no módulo

def all_global():
    global x        # declara globais atribuídas
    x = y + z       # não precisa declarar y, z: regra LEGB

# y e z são globais porque não foram atribuídas dentro da função

# ======================//======================

"""



"""