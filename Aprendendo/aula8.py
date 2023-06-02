var = True

print(var)

var = 10 < 15 # a variável 'var' armazena um valor booleano (True)

print(var)

var = 10 > 15 # a variável 'var' armazena um valor booleano (False)

print(var)

s = "socorro"

# ao converter uma string para tipo bool, é possível ver se a string está vazia ou não
print(bool(s)) # retorna True, pois a variável está armazenando uma string

s = ""

print(bool(s)) # retorna False, pois a variável não está armazenando uma string

var = 1 # quando convertido para bool, é True
var = 0 # quando convertido para bool, é False; qualquer número diferente de 0 será True

# é possível verificar, a partir da conversão para bool, se listas, tuplas, entre outros, estão ou não vazios