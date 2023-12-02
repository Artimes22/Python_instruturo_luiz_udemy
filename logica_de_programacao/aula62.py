"""
Calculo do segundo digito do CPF:

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores po uma
contagem regressiva começando de 11

Ex.: 746.824.890-70 (74682489070)
    11 10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0  7
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 363
Multiplicar o resultado anterior po 10
301 * 10 = 3630
obter o resto da divisão da conta anterior po 11
3630 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrario disso:
    resultado é p valor da conta

O primeiro dígito do CPF é 7    
"""

#primeiro digito do CPF
cpf_enviado_usuaruio = '74682489070'
nove_digitos = cpf_enviado_usuaruio[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

#segundo digito do CPF

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'


if cpf_enviado_usuaruio == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuaruio} é valido')
else:
    print('CPF invalido')    