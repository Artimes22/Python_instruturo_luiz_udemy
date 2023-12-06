"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma (x, y, z): #Parametro
    #Definição da função
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z )

soma(1, 2, 3) #Argumento posicional
soma(2, 1, 4)
soma(y=4, x=2, z=1) #Argumento nomeado
soma(4, 2, z=8)