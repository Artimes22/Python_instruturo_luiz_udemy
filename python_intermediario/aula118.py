# Ptoblema dos parâmetros mutáveis em funções Python

def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1=adiciona_cliente('Luiz')
adiciona_cliente('Joana', cliente1)
print(cliente1)

cliente2=adiciona_cliente('Helena')
adiciona_cliente('Maria', cliente2)
print(cliente2)