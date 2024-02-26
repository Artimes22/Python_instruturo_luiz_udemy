# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou regitros de
# bases de dados, etc.
# As namedtuples são imutáveis como as tuplas.

# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults = ['VALOR', 'NAIPE']    
# )

# as_espadas = Carta('A', 'Espadas')

# print(as_espadas._asdict())

# # print(as_espadas)
# # print(as_espadas.valor)
# # print(as_espadas.naipe)

from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A')
print(as_espadas)