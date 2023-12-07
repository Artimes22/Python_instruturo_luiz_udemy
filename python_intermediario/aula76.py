"""
Dicionários em python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas cmo o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves -{}- ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Luis otávio,
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'taltal', 'número': 123},
        {'rua': 'taltal', 'número': 456},
    ]
}
print(pessoa, type(pessoa))
"""
# pessoa = {
#     'nome': 'Luis otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'taltal', 'número': 123},
#         {'rua': 'taltal', 'número': 456},
#     ],
# }
# # print(pessoa, type(pessoa))
# # print(pessoa['idade'])

# for chave in pessoa:
#     print(chave, pessoa[chave])


# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'Artimes de Lima'
# pessoa['sobrenome'] = 'Miranda'

# print(pessoa[chave])
# pessoa[chave] = 'Maria'

# print(pessoa)
# del pessoa['sobrenome']
# print(pessoa)

# if pessoa.get('sobrenome', )is None:
#     print('NÃO EXISTE')
# else:
#     print(pessoa['sobrenome'])    

# print('ISSO NÃO VAI ')  



#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=   




"""
Métodos úteis dos dicionários em Python
len       - quantas chaves
keys      - iterável com as chaves
values    - iterável com os valores
items     - itterável com chaves e valores
setdefalt - adciona valor se a chave não existe
copy      - retorna uma cópia rasa (shallow copy)
get       - obtém uma chave
pop       - apaga um item com a chave especificada (del)
popitem   - apaga o útimo item adicionado
update    - atualiza um dicionário com outro 
"""

# pessoa = {
#     'nome': 'Luis otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
# }    

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# pessoa.setdefault('idade', 18)
# print(pessoa['idade'])


# for chaves in pessoa:
#     print(chaves)

# for valor in pessoa.values():
#         print(valor)

# for chave, valor in pessoa.items():
#     print(f'{chave}:', valor)


#-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-


# import copy #podera fazer uma copia completa do dicionário

# d1 = {
#   'c1' : 1,
#   'c2' : 2,
#   'c3' : 3,
#   'l1': [0, 1, 2]
# } 

# # d2 = d1 (indica o mesmo dicionário, se alterar o d2 tambem vai alterar o d1)

# #d2 = d1.copy() #copia tudo que for ímutavel do dicinario 
# #               tornadno um idependente do outro mas se dentro do dicionário
# #               tiver um ítem mutável tipo list, dict ele vai manter esses dados
# #               se alterados vai alterar nos dois dicionários
# #d2['c1'] = 1000
# #d2['l1'][1] = 9999
# print(d1)
# #print(d2)
# d2 = copy.deepcopy(d1)#vai poder entrar em todas as subcamadas e fazer alteração
#                       # em todos os itens imutáveis e mutáveis em todos os niveis 

# d2['c1'] = 1000
# d2['l1'][1] = 9999
# print(d2)

#-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1.get('nome', 'não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

print(p1)
p1.update({
    'nome': 'Artimes',
    'idade': 23,
    
})
print(p1)
