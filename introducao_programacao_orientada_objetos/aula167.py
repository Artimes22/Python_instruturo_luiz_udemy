# locale para internacionalização

import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(calendar.calendar(2022))
print(locale.getlocale())