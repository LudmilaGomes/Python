# Sobre escopo de variáveis

x = y = z = 0   #variáveis globais
mens = "Bom dia."

def imprimeMensagem():
    #mens2 = "Boa tarde."
    global mens3           # é preciso declarar a variável como 'global' indicando escopo de programa
    mens3 = "Boa noite."    # a variável só pode ser inicializada depois
    print(mens)

#print(mens2)   #não é possível imprimir 'mens2' fora do bloco da função acima, pois 'mens2' tem escopo de bloco e
#               só pode ser chamada novamente apenas dentro do bloco onde foi declarada

imprimeMensagem()   # a função precisa ser chamada para que 'mens3' exista

print(mens3)    # agora sim 'mens3' pode ser chamada fora do bloco em que foi declarada