"""
Calculo do primeiro digito do CPF:

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores po uma
contagem regressiva começando de 10

Ex.: 746.824.890-70 (74682489070)
    10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior po 10
301 * 10 = 3010
obter o resto da divisão da conta anterior po 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrario disso:
    resultado é p valor da conta

O primeiro dígito do CPF é 7    
"""

#primeiro digito do CPF
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = ((resultado_digito_1 * 10) % 11)
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)




