# Implemantando o protocolo do Itertator em Python
# Essa é apenas uma aula para introduzir os protocolos de collectios.abc no
# Python. Qualquer outro protocolo poderá ser implementado seguindo a mesma
# estrutura usada nessa aula.

from collections.abc import Sequence
from typing import Iterator

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        print('getitem', index)
        return self._data[index]
    
    def __setitem__(self, index, value):
        print('setitem', index)
        self._data[index] = value
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self._next_index >= self._index:
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value

if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria')
    lista.append('João')
    # print(lista._data)
    # print(lista[1])
    for item in lista:
        print(item)