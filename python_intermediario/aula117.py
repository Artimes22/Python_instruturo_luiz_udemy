import json

# pessoa = {
#     'nome': 'Luiz otávio',
#     'Sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'r1', 'numero': 32},
#         {'rua': 'r2', 'numero': 55},
#     ],
#     'Altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa,
#              arquivo,
#              ensure_ascii=False,
#              indent=2,
#              )
    
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])