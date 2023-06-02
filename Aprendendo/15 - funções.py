# FUNÇÕES - 15

"""

Funções são pacotes de código que podem ser chamados repetidamente,
com diferentes entradas e sáida a cada vez. Já chamamos funções antes,
mas o foco agora é o desenvolvimento de funções definidas pelo usuário.

Uma função agrupa um conjunto de instruções, de modo que elas podem
ser executadas mais de uma vez em um programa. As funções também nos
permitem especificar parâmetros que servem como entradas e podem diferir
a cada vez que o código da função é executado.


Chamadas:       minhaFuncao('parâmetro1', 'parâmetro2', 'parâmetro3')
def, return:    def func(a, b = 1 * c): return a + b + c[0]
global          def funcao(): global x; x = 'new'
lambda          funcs = [lambda x: x ** 2, lambda x: x * 3]

"""

# soma + 1 à variável X
from os import times

def incrementa(x):
    return x + 1

a = 12
print("Valor de 'a' antes da chamada da função: " + str(a))
a = incrementa(a)
print("Resultado da primeira função: " + str(a))

"""

Mas porque usar funções?
Reutilização de código: funções são a maneira mais simples de se empacotar
lógica que você precisa usar em mais de um lugar e mais de uma vez.

Decomposição procedural: as funções também fornecem uma ferramenta
para dividir os sistemas em partes, com tarefas bem definidas, pois
é mais fácil implementar subtarefas de um grande processo, já que vamos
implementar tarefas menores e não o processo inteiro de uma vez.


As funções se comportam de maneira diferente em Python, em relação ao
que acontece em linguagens compiladas, como C. Veremos que:

'def' é código executável:
A função que você cria não existe até que o Python busque e execute
a instrução def.

'def' cria um objeto e atribui um nome a ele:
Quando o Python busca e executa uma instrução def, ele gera um novo
objeto e atribui a ele o nome da função a ele. Assim, o nome da função
se torna uma referência para o objeto função.

'return' envia um objeto resultado de volta para quem fez a chamada:
Quando uma função é chamada, quem a chamou é interrompido até que ela
termine seu trabalho e retorne o controle. As funções que calculam um
valor o enviam de volta para quem fez a chamada com uma instrução 
return; o valor retornado torna-se o resultado da chamada de função.

argumentos passados por atribuição (referência de objetos):
No Python, os argumentos são passados para as funções por atribuição.

'global' declara variáveis em nível de módulo que devem ser atribuídas:
Por padrão, todos os nomes atribuídos em uma função são locais para
essa função, e existem apenas enquanto a função é executada. Para
atribuir um nome no módulo que as envolvem, as funções precisam listá-lo
em uma instrução global.

argumentos, valores de retorno e variáveis não são declarados:
Não há nenhuma restrição de tipo nas funções. Então, nada a respeito
de uma função precisa ser declarado antecipadamente; assim, podemos
passar argumentos de qualquer tipo, retornar qualquer tipo de objeto,
etc.


Instruções 'def'
A instrução def cria um objeto função e atribui um nome a ele.

 def <nome>(arg1, arg2, ..., argN):
     <instruções>
     ...
     return <valor>

A instrução return pode aparecer em qualquer parte no miolo de uma
função; ela finaliza a chamada de função e envia um resultado de volta
para quem fez a chamada. A instrução return é opcional; se não estiver
presente, a função termina quando o fluxo de controle chega no final
do seu miolo. Tecnicamente, uma função sem instrução return retorna
o objeto None automaticamente, mas normalmente ele é ignorado.


A instrução def é executada em tempo de execução
A instrução def é muito parecida com uma instrução '=': ela simplesmente
atribui um nome em tempo de execução. Ao contrário de linguagens compiladas
as funções do Python não precisam ser totalmente definidas antes que
o programa execute.

 outronome = funcao     # atribui o objeto função
 outronome()            # chama 'funcao' novamente

Aqui, a função recebeu um nome diferente e foi chamada por meio deste
novo nome. Assim como tudo em Pytho, as funções são apenas objetos; elas
são gravadas explicitamente na memória, no momento da execução do programa.

"""

# multiplica os valores X e Y (parâmetros)
def multiplica(x, y):   # cria e atribui função
    return x * y        # corpo executado quando chamado

"""

Quando o Python busca e executa essa instrução def, ele cria um novo
objeto função que empacota o código da função e atribui ao objeto o
nome 'multiplica'. Normalmente, essa instrução é escrita em um arquivo
de módulo e seria executada quando o arquivo que a contém fosse importado.


Chamadas
Após a execução da instrução def, o programa pode chamar (executar)
a função adicionando parênteses após seu nome. Opcionalmente, os parênteses
podem conter um ou mais argumentos de objeto, a serem passados para
os nomes no cabeçalho da função.

"""

# argumentos estão entre os parênteses
print("Resultado da segunda função: " + str(multiplica(2, 4)))

# podemos salvar o objeto resultado
x = multiplica(2, 4)

# as funções são 'sem tipo'
print("Resultado da segunda função: " + str(multiplica("Ni", 4)))

"""

Nesta terceira chamada, uma string e um inteiro são passados para X
e Y, em vez de dois números, e '*' funciona com números e com sequências.

"""

# ======================//======================

"""

Polimorfismo no Python:

O significado real de 'x * y' na função multiplica() depende completamente
dos tipos de objetos que x e y são.

Em muitas funções, o Python deixa por conta dos objetos fazer algo razoável
com a sintaxe. Assim, dependendo do tipo do objeto passado para a função, as
operações realizadas podem variar. Esse tipo de comportamento é conhecido 
como Polimorfismo (o significado das operações depende dos objetos que estão
sendo utilizados). Como o Python é uma linguagem tipada dinamicamente, o
polimorfismo corre solto: toda operação é polimórfica em Python.

Isso contribui muito para a flexibilidade da linguagem. Uma única função
geralmente pode ser aplicada a toda uma categoria de tipos de objeto. Contanto
que esses objetos suportem a interface (ou protocolo) esperada, eles podem
ser processados pela função.

Então, em multiplica(), quaisquer dois objetos que suportem um operador *
funcionarão. Se os objetos passados não suportam a operação, o Python detecta
o erro e lança uma exceção automaticamente.

Assim, de modo geral, desenvolvemos funções para interfaces de objetos no
Python e não para tipos de dados.

"""

# ======================//======================

"""

Segundo exemplo: intersecção de sequências

"""

# retorna uma lista com os valores que estão presentes simultaneamente
# na sequência1 e na sequência2, ou seja, a intersecção;
def intersect(seq1, seq2):
    res = []                # começa vazio   
    for x in seq1:          # percorre os elementos de seq1
        if x in seq2:       # se o elemento de seq1 estiver em seq2:
            res.append(x)   # adiciona o elemento da intersecção
    
    return res              # retorna a lista dos elementos em intersecção

s1 = "SPAM"
s2 = "SCAM"
# intersecção entre "SPAM" e "SCAM": ["S", "A", "M"]
print(intersect(s1, s2))

"""

Polimorfismo (de novo :D)

Assim como  todas as funções de Python, intersect() é polimórfica, ou seja,
ela funciona em tipos arbitrários, contanto que eles suportem a interface
do objeto esperada:

 x = intersect([1, 2, 3], (1, 4))   # x = [1]

No exemplo acima, passamos para a função tipos de objetos diferentes (lista
e tupla) e ela ainda distingue os itens comuns.

Para intersect, o primeiro argumento então, tem de suportar o loop for e o
segundo tem de suportar o teste de participação como membro 'in'. Se você
passar objetos que não suportam essas interfaces (como números), o Python
detectará automaticamente a combinação inadequada e lançará uma exceção.


Variáveis locais

A variável 'res' dentro da função intersect é o que, em Python, chamamos de
variável local - um nome visível apenas para o código que está dentro da função
def, e que só existe enquanto a função é executada. Na verdade, como todos
os nomes atribuídos de qualquer maneira dentro de uma função são classificados
como variáveis locais, por padrão, praticamente todos os nomes em intersect
são também variáveis locais.

 - res é uma variável local (ela é claramente atribuída dentro do def);
 - como os argumentos são passados por atribuição, seq1 e seq2 também são;
 - como o loop for atribui itens a uma variável, o nome x também é;

Todas essas variáveis locais aparecem quando a função é chamada e desaparecem
quando a função termina - instrução return, no final de intersectm envia de
volta o objeto resultado, mas o nome 'res' desaparece.

"""