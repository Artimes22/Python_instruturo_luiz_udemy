# nome = 'Artimes'

# # print(nome[2])
# # print(nome[-4])

# print('á' in nome)
# print('r' in nome)
# print('Art' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')    