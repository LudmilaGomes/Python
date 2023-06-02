x = 1           #inteiro
x = "hello"     #string
x = 3.14        #float
x = False       #bool

y = 5; z = 2; x = complex(y, z) #declaração de um número complexo (função)

#print(x)
#print(x.real)  #para imprimir a parte real do número
#print(x.imag)  #para imprimir a parte imaginária do número

x = ["carro", "avião", "navio", 1, 3.14, False] #list/array

#print(x[0])

x = ("carro", "avião", "navio", 1, 3.14, False) #tupla
#x[0] = "ônibus"  #- Não é possível alterar ou adicionar elementos

x = range(0, 101, 2) #inicia automaticamente um array que vai de 0 a 100, excluindo o 100, de 2 em 2 

#print(x[0]) #imprime 0
#print(x[1]) #imprime 2

x = { # dict
    "nome": "Ludmila",
    "idade": 18,
    "dataNasc": "04/11/2003"
}

#print("Valor: " + x["nome"])
#print("Valor: " + str(x["idade"]))
#print("Valor: " + x["dataNasc"])

x = {5, 3, 8, 5, 7, 9, 1, 2, 6} #set
x = frozenset({5, 3, 8, 5, 7, 9, 1, 2, 6}) #frozenset não permite alterar o set

# quando o set é impresso, apesar de possuir dois elementos de mesmo valor, os repetidos não é mostrado

print("Valor de x: " + str(x))      #conversão de x de inteiro para string
print("Tipo de x: " + str(type(x)))   #conversão do tipo 'type' para string