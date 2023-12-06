"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
"""

x = 1

def escopo():
    x = 10
    def outra_funcao():
        x = 12
        y=2
        print(x, y)
    
    outra_funcao()
    print(x)

escopo()
print(x)