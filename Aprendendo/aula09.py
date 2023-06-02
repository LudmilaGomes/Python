# LIST/ARRAY

comidas = ["cuscuz", "pizza", "macarrão", "feijão"]

print(comidas[0])   # primeiro elemento da lista
print(comidas[1])   # segundo elemento da lista
print(comidas[-1])  # primeiro elemento da lista (da direita para a esquerda)
print(comidas[-2])  # segundo elemento da lista (da direita para a esquerda)

comidas[2] = "arroz" # mudança de um dos elementos da lista

print(comidas)

comidas.append("feijoada") # adiciona um elemento à lista

print(comidas)

print( str(len(comidas) ) + " comidas na lista" ) # len(comidas) retorna o tamanho da lista 'comidas'

comidas.remove("arroz") # remove um elemento da lista
comidas.pop()           # remove o último elemento da lista
del comidas[0]          # remove o elemento na posição indicada da lista

comidas.clear()         # remove todos os elementos da lista

print(comidas)

comidas = ["cuscuz", "pizza", "macarrão", "feijão"]
comidas2 = list(comidas) # uma lista recebendo os elementos de outra lista já existente

print(comidas)
print(comidas2)

comidas2 = ["farinha de mandioca"]

comidas3 = comidas2 + comidas # 'comidas3' recebe os elementos das outras duas listas

print(comidas3)

