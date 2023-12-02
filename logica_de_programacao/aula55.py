"""
Imprecisão de ponto flutuante
utiliza "decimal.Decimal" so quando for necessario 
utilizar um numero muito grande ex. 0.000000123456
outras situações a formatação ja vai ser suficiente
para mostrar o numero correto
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))