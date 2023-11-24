primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Difite outro valor: ')

primeiro_valor1 = int(primeiro_valor)
segundo_valor2 = int(segundo_valor)

if primeiro_valor1 > segundo_valor2:
    print(f'O primeiro valor = {primeiro_valor1} é maior que o segundo valor = {segundo_valor2}')
elif segundo_valor2 > primeiro_valor1:
    print(f'O segundo valor = {segundo_valor2} é maior que o primeiro valor = {primeiro_valor1}')
elif primeiro_valor1 == segundo_valor2:
    print('Os dois valores são iguais')    