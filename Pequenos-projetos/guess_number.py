# geração de um número aleatório e contagem de 
# quantas tentativas o usuário teve até acertar o número

# importa o módulo 'random' e permite usar suas funçõe
import random
import os

os.system('cls')

"""

No módulo 'random', podemos usar a função 'randrange()'. Esta função irá gerar um valor aleatório
que está dentro do intervalo especificado da seguinte forma:

    random.randrange(start, stop, step)

em que 'start' é o valor inicial, 'stop' é o valor final e 'step' determina o valor de incremento,
sendo de uso opcional e tendo como valor padrão 1. Além disso, consideramos que o valor 'stop' não 
está dentro do intervalo considerado. Assim, temos:

    random.randrange(0, 10)                 # valor aleatório no intervalo [0, 10) ou [0, 9]
    random.randrange(10)                    # valor aleatório no intervalo [0, 10) ou [0, 9]
    random.randrange(0, 10, 2)              # valor aleatório dentro de [0, 2, 4, 6, 8]
    random.randrange(0, 10, 3)              # valor aleatório dentro de [0, 3, 6, 9]
    valor = random.randrange(0, -10)        # erro! Isto não funciona com randrange()
    valor = random.randrange(0, -10, -1)    # definindo o 'step', isso passa a funcionar!

A função 'randint()', também do módulo random, é muito semelhenate a 'randrange'. As diferenças estão
no fato de randint() não ter como parâmetro o 'step' para incremento e o valor do 'stop' é considerado,
ou seja, está dentro do intervalo. Assim:

    random.randint(0, 10)       # valor aleatório no intervalo [0, 10]
    random.randint(10)          # erro! Isto não funciona com randint(); falta um parâmetro
    random.randint(0, 10, 2)    # erro! Isto não funciona com randint(); há apenas dois parâmetros, um terceiro é um erro
    random.randint(0, -5)       # erro! Isto não funciona com randint(); com incremento padrão de 1, -5 nunca será alcançado

# Código para teste 
valor = random.randrange(-5, 11) # valor aleatório está nesse intervalo: [-5, 11) ou [-5, 10]
print(valor)

valor = random.randint(-5, 11) # valor aleatório está nesse intervalo: [-5, 11]
print(valor)

"""

print("Vamos jogar um jogo! Você irá adivinhar qual o número dentro de um intervalo de 0 a ..., ", end="")
print("pois é você quem diz qual o valor final do intervalo!")
print()

final_intervalo = input("Digite o número: ")

# precisamos verificar se o que foi digitado pelo usuário é um número positivo

if not(final_intervalo.isdigit()):
    # laço de repetição que se repete até o usuário digitar um valor apropriado
    while not(final_intervalo.isdigit()):
        final_intervalo = input("Digite um valor numérico positivo: ")

if int(final_intervalo) <= 0:
    # laço de repetição que se repete até o usuário digitar um valor apropriado 
    while int(final_intervalo) <= 0:
        final_intervalo = input("Digite um valor numérico positivo: ")

print()
print("O número aleatório está dentro do intervalo: [0, %d]" % int(final_intervalo))
print()

"""

Usamos 'int(final_intervalo)' pois randint() recebe como parâmetros valores inteiros e,
por padrão, a função input() recebe um dado do tipo string; assim, 'final_intervalo' é um
número, mas está no formato de string.

int("25") => 25

"""
numero_aleatorio = random.randint(0, int(final_intervalo))
#print(numero_aleatorio)

quant_tentativas = 0 # contador da quantidade de tentativas do usuário para acertar o número aleatório

while 1:
    numero_usuario = input("Agora, tente adivinhar o número: ")
    # testamos se a entrada é um número positivo
    if not(numero_usuario.isdigit()):
        while not(numero_usuario.isdigit()):
            numero_usuario = input("Digite um valor numérico positivo: ")

    if int(numero_usuario) <= 0:
        while int(numero_usuario) <= 0:
            numero_usuario = input("Digite um valor maior que zero: ")

    numero_usuario = int(numero_usuario)

    # agora, testamos se o usuário acertou o número aleatório
    if numero_usuario == numero_aleatorio:
        print("Parabéns! Você finalmente acertou!")
        break
    else:
        quant_tentativas += 1
        if numero_usuario < numero_aleatorio:
            print("Oops, você errou! Tente novamente. Mas saiba que o seu chute é menor que o número aleatório.")
        else:
            print("Oops, você errou! Tente novamente. Mas saiba que o seu chute é maior que o número aleatório.")

print("Fim de jogo! Você acertou o número aleatório %d em %d tentativas!" % (numero_aleatorio, quant_tentativas))