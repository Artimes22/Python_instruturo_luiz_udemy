nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print()

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('O seu nome contém espaços')
    else:
        print('Seu nome NÂO contem espaços')
    print(f'Seu nome tem {len(nome)} letras')            
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpa, você deixou os campos vazios')    
