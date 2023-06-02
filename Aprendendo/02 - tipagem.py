# TIPAGEM DINÂMICA - 2

"""

Em Python, os tipos das variáveis são determinados automaticamente, em tempo de execução, e não em resposta às declarações 
presentes em seu código. Assim, nunca é preciso declarar variáveis antecipadamente.

Com 

 a = 3

estamos criando uma variável que armazena o valor 3. Mas, ao contrário de C, 'a' é apenas um nome, e esse nome referencia
o objeto '3', que está armazenado em um trecho de memória. Assim, quando temos:

 a = 3
 a = 'spam'

A variável 'a' não está mudando de tipo. A variável 'a' é simplemente um nome para uma variável, e essa variável, na segunda
instrução passa a referenciar um outro trecho de memória que armazena a string 'spam'. Então, ao declarar uma variável, estamos
criando um objeto para representar o 3, criando a variável a e, por fim, vinculando a variável 'a' ao novo objeto '3'. As 
variáveis sempre são vinculadas a um objeto.

variáveis: são entradas em uma tabela de pesquisa, com espaço para vínculo para um objeto; são sempre ponteiros para objetos;
objetos: são partes de memória alocada, com espaço para representar o valor que denotam e informações de tag de tipo.

 a = 3
 b = a
 a = 5

Criamos a variável 'a' que aponta para o objeto '3' do tipo inteiro; criamos a variável 'b' que também aponta para o objeto '3';
em seguida, fazemos a variável 'a' apontar para um novo objeto, o objeto '5' de tipo inteiro. O objeto '3' já criado permanece 
na memória, ele não é alterado mas, é criado um novo objeto '5' em outro espaço de memória. Inteiros nunca podem ser alterados
no local - uma propriedade chamada imutabilidade.

Mas, existem objetos e operações que realizam alterações em objetos no local. Por exemplo, a atribuição de deslocamentos em listas
realmente altera o objeto do tipo lista (no local) em si, em vez de gerar um novo objeto. 

"""

# são duas variáveis que apontam (referenciam) para o mesmo objeto (referências compartilhadas);
l1 = [2, 3 , 4]
l2 = l1

# assim, quando alteramos um valor da lista em l1, l2 também sofre a alteração, pois l1 e l2 referenciam o mesmo objeto;
l1[0] = 49
print(l2)

"""

Quando os nomes referenciam novos objetos, o Python também recupera o objeto antigo, caso ele não seja referenciado por nenhum outro nome.
essa recuperação automática do espaço do objeto é conhecida como 'coleta de lixo'. Assim, podemos usar os objetos livremente, sem nos preocuparmos
com o uso de memória.

 x = 123
 x = 3.14   # Recupera 123

O objeto '123' será recuperado imediatamente, contanto que não seja referenciado em nenhum outro lugar - o espaço do objeto é devolvido
automaticamente e pode ser reutilizado por um futuro objeto.

Tecnicamente, para certos tipos, este comportamente de coleta pode ser mais conceitual do que literal, pois o Python reutiliza inteiros
e strings pequenas. Então, o objeto '123' provavelmente não será recuperado.

"""