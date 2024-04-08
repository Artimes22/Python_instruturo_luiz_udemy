# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretorios de 
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretorio atual (root), uma lista de subdiretorios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join('/Users','Usuario', 'Documents', 'Artimes', 'estudos')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir', dir_)
    for file_ in files:
        print('  ', the_counter, 'Files', file_)