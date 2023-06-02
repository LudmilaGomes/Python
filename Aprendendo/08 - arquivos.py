# ARQUIVOS - 8

"""

A função interna 'open' cria um objeto arquivo do Python, o qual serve 
como um vínculo para um arquivo residente em seu computador. Após chamar
open, você pode ler e gravar o arquivo externo associado, chamando métodos
do objeto arquivo. 

O nome interno 'file' é sinônimo de open e os arquivos podem ser abertos
chamando-se qualquer um desses nomes.

Os objetos arquivo são incomuns e em comparação com os tipos já vistos.
Eles vão exportar métodos apeas para tarefas comuns de processamento
de arquivos.

 output = open('/tmp/spam', 'w')    # cria arquivo de saía (w - write)
 input = open('data', 'r')          # cria arquivo de entrada (r - read)
 s = input.read()                   # lê o arquivo inteiro em uma string
 s = input.read(N)                  # lê N bytes
 s = input.readline()               # lê a próxima linha (até o \n)
 l = input.readlines()              # lê o arquivo inteiro na lista de strings da linha
 outuput.write(s)                   # grava a string s no arquivo
 outuput.writelines(l)              # grava no arquivo todas as strings da linha da lista l
 outuput.close()                    # fechamento manual

"""

# ================================//================================
# ARQUIVOS EM AÇÃO

meuArquivo = open('meu Arquivo.txt', 'w')
meuArquivo.write("Olá, mundo dos arquivos em Python!!!\n")
meuArquivo.close()
# e funcionou :)

meuArquivo = open('meu Arquivo.txt', 'r')
print(meuArquivo.readline())
# e funcionou :D