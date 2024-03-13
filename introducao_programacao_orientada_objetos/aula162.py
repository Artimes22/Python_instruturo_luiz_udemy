# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# datetime.fromtimestamp(Unix Timestamp)
# Para timezones

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# from pytz import timezone


# data = datetime(2023, 3, 4)
# data_str_fmt = '%d/%m/%Y'

# data_str_data = '2024/03/04 16:25:48'
# print(data_str_data)
# data_str_data = '04/03/2024'
# print(data_str_data)
# data = datetime.strptime(data_str_data, data_str_fmt)

# data = datetime.now(timezone('America/Sao_Paulo'))

# data = datetime.now()
# print(data.timestamp())

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = timedelta(days=10)
print(data_fim + delta)
print(data_fim + relativedelta(seconds=60))
# delta = data_fim - data_inicio/
# print(delta.days, delta.seconds, delta.microseconds)