# TESTES IF - 13

"""

A instrução 'if' do Python é típica da maioria das linguagens procedurais.
Ela assume a forma de um teste if, seguido de um ou mais testes elif
opcionais (significando "else if"), e termina com um bloco opcional
else. Cada teste e a cláusula else têm um bloco associado de instruções
aninhadas, indentadas sob uma linha de cabeçalho.

 if <teste 1>:
    <instruções>
 elif <teste 2>:
    <instruções>
 else:
    <instruções>

Em Python, não há nenhuma instrução "switch" ou "case". Em vez disso,
o desvio de vários caminhos é codificado como uma série de testes if/elif
ou pela indexação de dicionários ou pesquisa em listas.

 escolha = input("Digite uma operação: ")

 operacoes = {"+" : "soma",
              "-" : "subtração",
              "*" : "multiplicação",
              "/" : "divisão" }
        
 print(operacoes[escolha])


Ou usando 'if':


 escolha = input("Digite uma operação: ")

 if(escolha == "+"):
     print("soma")
 elif(escolha == "-"):
     print("subtração")
 elif(escolha == "*"):
     print("multiplicação")
 elif(escolha == "/"):
     print("divisão")
 else:
     print("Operação inválida")

Aqui, a cláusula 'else' é usada para tratar do caso em que nenhuma 
chave corresponde.

Abaixo, está um exemplo de como tratar o caso em que nenhuma chave 
corresponde quando usamos o dicionário.

"""

almoço = {"feijão" : "1 kg", "macarrão" : "1 kg", "arroz" : "1 kg"}

# usamos o 'get()'; primeiro argumento é a chave; segundo argumento é o que será impresso se não existir a chave
print( almoço.get("feijão", "má escolha") )
print( almoço.get("carne", "má escolha") )

# ======================//======================

"""

Em geral, o Python tem uma sintaxe simples. Mas existem algumas propriedades
importantes:

As instruções são executadas uma após a outra, até que digamos o contrário.
Normalmente, o Python executa as instruções de um arquivo ou bloco aninhado
da primeira até a última instrução, mas instruções como o if fazem o 
interpretador saltar em seu código. Assim, o 'if' é uma instrução que
pode alterar o fluxo de controle (é assim que chamamos o fluxo de execução
natural dos programas em Python). Assim, comandos que afetam esse fluxo
são chamados de instruções de controle de fluxo.

Os limites de blocos e instruções são detectados automaticamente pelo
Python. Não usamos chaves ou delimitadores em torno de blocos de código.
Também não usamos ponto-e-vírgula ao fim das linhas.

Instruções compostas = cabeçalho. ":", instruções indentadas. Em Python,
todas as instruções compostas seguem o mesmo padrão: uma linha de
cabeçalho terminada com dois-pontos, seguida de uma ou mais instruções
aninhadas, indentadas sob o cabeçalho.

Normalmente, linhas em branco, espaços e comentários são ignorados.

Strings de documentação são ignoradas, mas são salvas e exibidas por
ferramentas. O Python suporta uma forma de comentário adicional chamada
string de documentação a qual é mantida. As 'docstrings' fazem parte
da documentação mais ampla do Python.

Sobre delimitadores de bloco:
O Python detecta os limites automaticamente pela indentação da linha, 
que é o espaço vazio à esquerda do código. Todas as instruções indentadas
com a mesma distância à direita pertencem ao mesmo bloco de código. ENtão,
as instruções dentro de um bloco são alinhadas verticalmente.

Sobre delimitadores de instrução:
Normalmente, as instruções terminam no fim da linha em que aparecem.
Isso abrange a ampla maioria das instruções em Python. Mas, quando as
instruções são longas demais para caberem em uma única linha, algumas
regras podem ser usadas para fazer com que elas se estendam por várias
linhas de continuação:

As instruções podem abranger várias linhas se você estiver continuando
um par sintático aberto. Ou seja, caso esteja codificando algo incluído
em pares (), [] e {}.

As instruções podem abranger várias linhas se terminarem com uma barra
invertida. 

 if a == b and c == d and \
    d == e and f == g:
     print("Socoro")

Como um caso especial, o Python permite você escrever mais de uma instrução
não composta (isto é, instruções não alinhadas) na mesma linha, separadas
por pontos-e-vírgulas.

 x = 1; y = 2; print(x)

E, por fim, o Python também permite que você mova o corpo de uma instrução
composta para a linha de cabeçalho, desde que o corpo seja apenas uma
instrução simples (não composta).

 if x == 1: print("Bom dia.")

Agora, sobre Testes de Verdade:

 - Verdadeiro significa qualquer número diferente de zero ou objeto 
não-vazio;
 - Falso significa não verdadeiro: um número zero, um objeto vazio ou
None;
 - As comparações e testes de igualdade são aplicados recursivamente
nas estruturas de dados;
 - As comparações e testes de igualdade retornam '1' ou '0' (no caso,
verdadeiro ou falso);
 - Os operadores booleanos 'and' e 'or' retornam um objeto operando
verdadeiro ou falso.

Em resumo, os operadores booleanos são usados para combinar os resultados
de outros testes. Então, temos:

X and Y
    É verdadeiro se X e Y são verdadeiros

X or Y
    É verdadeiro se X ou Y é verdadeiro

not X
    É verdadeiro se X é falso

"""