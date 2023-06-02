lComidas = ["cuscuz", "farofa", "biscoito"]

lComidas[0] = "pizza"

for x in lComidas:
    print(x)

# ==============================//==============================

tComidas = ("cuscuz", "farofa", "biscoito")

# tComidas[0] = "pizza" - os elementos de uma tupla não podem ser alterados após a declaração da tupla (no caso, diretamente na tupla)

for z in tComidas:
    print(z)

# ==============================//==============================

tComidas2 = ("cuscuz", "farofa", "biscoito")

print(tComidas2)

lComidas2 = list(tComidas2)
lComidas2[0] = "pizza"
tComidas2 = tuple(lComidas2)

print(tComidas2)