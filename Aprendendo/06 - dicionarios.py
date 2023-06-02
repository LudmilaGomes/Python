# DICIONÁRIOS - 6

"""

Como as listas, dicionários também é um tipo do Python muito flexível. Mas, ao contrário das listas, que são coleções ordenadas, os
dicionários seriam coleções desordenadas; nos dicionários, os itens são armazenados e buscados pela chave, em vez do deslocamento
posicional.

Dicionários são acessados pela chave e não pelo deslocamento, coleções desordenadas de objetos arvitrários, têm comprimento variável,
são heterogêneos, podem ser aninhados arbitrariamente e pertencem à categoria de mapeamento mutável.

Os dicionários são escritos como uma série de pares chave : valor, separados por vírgulas e incluídos entre chaves:

 dictionary = { "uma comida" : "lasanha", "nome" : "Ludmila", "idade" : 18 }

"""

# ================================//================================
# DICIONÁRIOS EM AÇÃO


d1 = {}                                                                     # dicionário vazio
d2 = {"nome" : "Ludmila", "idade" : 18}                                     # dicionário de dois itens
d3 = { "café da manhâ" : {"pão" : 2, "xícaras de café" : "todas"} }         # aninhamento
print(d2["nome"])                                                           # indexação por chave
print(d3["café da manhâ"]["xícaras de café"])       

len(d2)                                                                     # comprimento do dicionário
d2["nome"] = "Ainda é Ludmila"                                              # alteração
del d3["café da manhâ"]["pão"]                                              # exclusão

# print(d2.has_key("nome"))                                                 # teste de participação da chave como mesmbro - não existe em Python 3
print("nome" in d2)                                                         # teste de participação da chave como mesmbro usando 'in'

listaChaves = d2.keys()                                                     # 
print(listaChaves)

"""
 -> HAS_KEY
O método 'has_key()' foi removido do Python 3, mas tinha mesmo objetivo do 'in'.

 -> KEYS
O método 'keys()' retorna uma lista com todas as chaves presentes no dicionário.

"""

# ================================//================================
# ALTERANDO DICIONÁRIOS NO LOCAL

"""

Os dicionários são mutáveis. Portanto, você pode alterá-los, expandi-los e diminuí-los no local, como as listas.

"""

dicionario = {"nome" : "Ludmila", "idade" : 18, "país" : "Brasil"}

dicionario["nome"] = ["Ludmila", "Gomes"]   # lista dentro de um dicionário
del dicionario["país"]                      # excluída entrada
dicionario["Quer ir à praia"] = ["sim"]     # adicionada nova entrada

print(dicionario)

# Outros métodos

"""

 -> VALUES
Retorna uma lista com os valores do dicionário.

 -> ITEMS
Retorna uma lista com tuplas compostas dos pares (chave : valor)

 -> GET
É usado para retornar um valor de uma chave dentro de um dicionário. Se a chave não existe no dicionário, retorna 'None'.

 -> UPDATE
Esse método fornece ao dicionário uma ferramenta semelhante à concatenação. Ele intercala as chaves e os valores de um dicionário
em outro, sobrescrevendo cegamente os valores da mesma chave.

"""

dicionario = {"nome" : "Ludmila", "idade" : 18, "país" : "Brasil"}
d2 = {"uma comida" : "pizza", "nome" : "Ludmila Gomes"}

print(dicionario.values())

print(dicionario.items())

print(dicionario.get("nome"))
print(dicionario.get("comida"))

dicionario.update(d2)
print(dicionario)

# Exemplo: aplicação do dicionário (Tabela de linguagens)

tabela = {  "Python"  : "Guido van Rossum", 
            "perl"    : "Larry Wall", 
            "Tcl"     : "John Ousterhout"     }

linguagem = "Python"
criador = tabela[linguagem]

print(criador)

print()

# 1ª forma
for linguagem in tabela.keys(): # relembrando: 'keys()' retorna uma lista com todas as chaves presentes no dicionário.
    print(linguagem + ", " +  tabela[linguagem])

# 2ª forma
for linguagem in tabela:
    print(linguagem + ", " +  tabela[linguagem])

# os formatos acima são equivalentes e funcionam da mesma maneira