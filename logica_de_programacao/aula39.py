nome = 'Artimes de Lima'

tamnho_nome = len(nome)

# print(nome)
# print(tamnho_nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}' 
    indice += 1

print(novo_nome)    