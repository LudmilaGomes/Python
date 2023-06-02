# LOOP FOR - laço de repetição

comidas = ["feijoada", "rubacão", "lasanha", "refrigerante", "pizza"]

# for: variável i em 'comidas' vai assumir o valor do elemento na posição comidas[0], comidas[1], comidas[2], comidas[3], comidas[4]
for i in comidas:
    print(i) # os elementos vão ser impressos na tela um de cada vez

# =============================//=============================

for i in "comidas":
    print(i)

# =============================//=============================

for i in comidas:
    print(i) # os elementos vão ser impressos na tela um de cada vez
    if i == comidas[2]:
        break
