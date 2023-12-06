"""
args - Argumentos não nomeados
* - * *args (empacotamento e desempacotamento)
"""
#Lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma (x, y):
#     return x + y

def soma(*args):
    total = 0 
    for numero in args:
        total += numero
    return total


# soma_1 = soma(1, 2, 3)    
# print(soma_1)
# soma_2 = soma(4, 5, 6)    
# print(soma_2)
# soma_3 = soma(7, 8, 9, 10, 15)    
# print(soma_3)

# print(sum((7, 8, 9, 10, 15)))
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
soma_4 = soma(*numeros)
print(soma_4)
print(numeros)
print(*numeros)
print(sum(numeros))