# Usando calendar para calendários e datas
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# Sendo 0 = segunda-feria e 6 = domingo

import calendar

# print(calendar.calendar(2024))
# print(calendar.month(2000, 2))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])

for week in calendar.monthcalendar(2022, 12):
    print(list(enumerate(week)))