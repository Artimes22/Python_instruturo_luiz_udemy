# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos 
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G', 'GG'],
    ['Masculino', 'Feminino'],
    ['Algodão', 'Poliéster'],
]
# print('Combinações')
# print_iter(combinations(pessoas, 2))
# print('Permutações')
# print_iter(permutations(pessoas, 2))
print('Produtos')
print_iter(product(*camisetas))

