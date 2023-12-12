# Try, except, else e finally
try:
    print('Abrir arquivo')
    8/0
except ZeroDivisionError:
    print('Dividiu zero')   
else: #Vai executar caso não ocorra erros no código
    print('Não ocorreu erros')     
finally: #Sempre será executado mesmo tendo algum erro
    print('Fechar arquivo')