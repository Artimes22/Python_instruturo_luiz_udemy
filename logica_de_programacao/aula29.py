numero_str = input('Informe um número: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')    

try:
    print('SRT', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')     