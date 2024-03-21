# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 ano.
# A data em que ela pegou o emprésstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela.

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parecelas = [] 
data_parecela = data_emprestimo
while data_parecela < data_final:
    data_parecelas.append(data_parecela)
    data_parecela += relativedelta(months=+1)

numero_parcelas = len(data_parecelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parecelas:
    print(data.strftime('%d/%m/%y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R${valor_total:.2f} para pagar '
    f'em {delta_anos.years} anos'
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}'

)