numero = input('Digite um número: ')

if numero.isdigit():
    numero_int= int(numero)
    par_impar = numero_int % 2 ==0
    par_impar_texto = 'Ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}') 
    
else:
    print('O número informado não é um número inteiro')


# print('=-'* 30)

# horas = input('Informe a hora: ')
# horas_int = int(horas)

# if horas_int >= 0 and horas_int <= 11:
#     print('Bom dia')
# elif horas_int > 11 and horas_int <= 17:
#     print('Boa tarde')
# elif horas_int > 17 and horas_int<= 23:
#     print('Boa noite')         

# print('=-'* 30)    

# nome = input('Informe seu primeiro nome: ')
# tamanho = len(nome)

# if tamanho <= 4:
#     print('Seu nome é pequeno')
# elif tamanho > 4 and tamanho <=6:
#     print('Seu nome é normal') 
# else:
#     print('Seu nome é muito grande')       