# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas çistas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     ]
print('Exercicio 1')
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(l1, l2))
print(list(zip(l1,l2)))
print()
print(list(zip_longest(l1,l2, fillvalue='SEM CIDADE')))

print()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print()
print('Exercicio 2')
# Considerando duas listas de interiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:

# Se uma lista for maior que a outra, soma só vai considerar o tamanho da
# menor.

# Exemplo:
# lista_a =    [1, 2, 3, 4, 5, 6, 7]
# lista_b =    [1, 2, 3, 4]

# lista_soma = [2, 4, 6, 8]

from itertools import zip_longest

# def soma_lista(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i] + lista2[i]) for i in range(intervalo_maximo)
#     ]    

lista_a =    [1, 2, 3, 4, 5, 6, 7]
lista_b =    [1, 2, 3, 4]
# lista_soma = soma_lista(lista_a, lista_b)
# print(lista_soma)
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)

lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)