while True:

    numero_1 = input('Informe um número: ')
    numero_2 = input('Informe outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:        
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos')     
        continue   

    operadores_permetidos = '+-/*'


    if len(operador) > 1:
        print('Digiter apenas 1 operador')     
        continue
    if operador not in operadores_permetidos:
        print('Operador invalido')     
        continue
    ###########

    print('Realizando sua conta. confira o resultado')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/': 
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria ter chegado até aqui.')         
    

    ###########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break