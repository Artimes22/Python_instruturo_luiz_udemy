"""
Valores padrão para parâmetros
Ao defenir uma função, os parametros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)        

soma(1, 2)    
soma(3, 5)    
soma(14, 23)    
soma(100, 200)    
soma(8, 7, 0)    
soma(8, 7, 5)    
