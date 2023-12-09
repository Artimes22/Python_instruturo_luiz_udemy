# Vlores Truthy e Falsy, tipos Mutávei e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
false = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE',  falsy('TESTE'))
print(f'{lista=}',  falsy(lista))
print(f'{dicionario=}',  falsy(dicionario))
print(f'{conjunto=}',  falsy(conjunto))
print(f'{tupla=}',  falsy(tupla))
print(f'{string=}',  falsy(string))
print(f'{inteiro=}',  falsy(inteiro))
print(f'{flutuante=}',  falsy(flutuante))
print(f'{nada=}',  falsy(nada))
print(f'{false=}',  falsy(false))
print(f'{intervalo=}',  falsy(intervalo))

#-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-
print()
print('-='*20)
print()
#-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-

lista = [ 0]
dicionario = { 0}
conjunto = set( '0')
tupla = ( 0, 'r')
string = 'r'
inteiro = 1
flutuante = 0.1
nada = None
false = True
intervalo = range(0, 2)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE',  falsy('TESTE'))
print(f'{lista=}',  falsy(lista))
print(f'{dicionario=}',  falsy(dicionario))
print(f'{conjunto=}',  falsy(conjunto))
print(f'{tupla=}',  falsy(tupla))
print(f'{string=}',  falsy(string))
print(f'{inteiro=}',  falsy(inteiro))
print(f'{flutuante=}',  falsy(flutuante))
print(f'{nada=}',  falsy(nada))
print(f'{false=}',  falsy(false))
print(f'{intervalo=}',  falsy(intervalo))