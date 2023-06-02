curso = "Curso de Python"
palavra = "Python"

# ambas (in e not in) retornam True/False, ou seja, um valor booleano
resultado = palavra in curso # verifica se a primeira string está presente na segunda string
print(resultado)

resultado = palavra not in curso # verifica se a primeira string NÃO está presente na segunda string
print(resultado)

s1 = "socorro, "
s2 = "meu deus"

sFinal = s1 + s2

print(sFinal)

cidade = "João Pessoa"
dia = 9
mes = "Julho"
ano = 2022

data = "{}, {} de {} de {}"

print(data.format(cidade, dia, mes, ano))