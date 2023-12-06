"""
Exercicios com funções

Crie uma função que multiplique todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor 
da variável.

Crie uma função que fala se o número é par ou ímopar.
Retorne se o número é par ou ímpar
"""



def multi(*args):
    multiplicacao = 1
    for numero in args:
        multiplicacao *= numero
    return multiplicacao

def par(numero):
    if numero % 2 == 0:
        return f'{numero} É par'
    else:
        return f'{numero} É ímpar'   


multiplicacao = multi(3,5,7,2)   
par_impar = par(multiplicacao)
print(par_impar)
