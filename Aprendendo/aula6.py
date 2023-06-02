s = "socorro" # string = lista de caracteres

print(s)        # imprime a string

print(s[0])     # imprime um elemento do array de caracteres/string

print(s[0:4])   # imprime os elementos dentro do intervalo
print(s[2:4])

print("Tamanho: " + str(len(s)) + " letras")

s = " socorro "

print(s)
print(s.strip()) # retira os espaços no começo e fim da string

s = "SOcoRRo"

print(s.lower()) # letras todas minúsculas
print(s.upper()) # letras todas maiúsculas

s = "curso de python"

print(s.replace("python", "C#")) # troca um caractere por outro, ou uma string por outra

print(s.split()) # split - retorna uma lista com as substrings de uma string, estas substrings separadas por espaços