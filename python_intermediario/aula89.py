# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper1'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)    