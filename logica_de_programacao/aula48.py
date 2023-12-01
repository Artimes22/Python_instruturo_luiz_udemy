"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - Ìndices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321

# string = 'ABCDE' # 5 caracteres
# #print(bool([])) #falsy
# #print(lista, type(lista)) 

# #         0     1       2       3    4
# #        -5    -4      -3      -2   -1      
# lista = [123, True, 'Artimes', 1.2, []]
# print(lista)
# lista[-3] = 'Maria'
# print(lista)

###############

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - Ìndices e fatiamento
Métodos úteis: 
    append:  Adiciona um item ao final
    insert:  Adiciona um item no índice escolido
    pop:     Remove do final ou do índice escolido
    del:     Apaga um índice
    clear:   Limpa a lista
    extend:  Estende a lista
    +:       Conecta lista
Create Read Upadate Delete
Criar  Ler  Alterar Apagar = lista[i] (CRUD)    
"""

# lista = [10, 20, 30, 40]
# # print(lista)
# # lista[2] = 300
# # print(lista)
# # del lista[1]
# # print(lista)

# lista.append(50)
# print(lista)
# lista.append(60)
# print(lista)
# lista.pop()
# lista.append(70)
# lista.append(80)
# print(lista)
# valor_removido = lista.pop(3)
# print(lista)
# print('Removido', valor_removido)

#######################

# lista.append('Artimes')
# nome = lista.pop()
# lista.append(1234)
# del lista[-1]
# lista.insert(0, 5)
# print(lista)

##########################

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_c)
# print(lista_c)
# print(lista_a)

##########################

"""
Cuidadods com dados mutáveis

= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""




