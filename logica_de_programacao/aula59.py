#Desempacotando em chamadas
#De métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

# a, b,*_, ap, c = lista
# print(a,ap)

# for nome in lista:
#     print(nome, end=' ') 
print(*lista)
print(*string)
print(*tupla)