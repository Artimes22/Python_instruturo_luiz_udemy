"""
Faça uma lista de compra com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []
while True:
    print('Selecione uma opção')
    acao = input('[I]nserir [A]pagar [L]istar: ')

    if acao == 'i':
        os.system('cls')
        novo_item = input('Valor: ')
        lista.append(novo_item)
        
    elif acao == 'l':   
        if len(lista) == 0:
            print('Nada para listar')

        for indice, item in enumerate(lista):
            print(indice, item)

    elif acao == 'a':
        excluir_item = input('Escolha o índice para apagar: ')
        # excluir_item = int(excluir_item)
        # if excluir_item == indice:
        #     lista.pop(excluir_item)
        # continue 
        #                 ERRADO
        try:
            indice = int(excluir_item)
            del lista[indice]
        except:         
            print('Produto inexistente')

    else:
        print('Por favor, escolha i, a ou l.')               

