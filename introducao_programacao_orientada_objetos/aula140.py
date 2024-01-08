# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> Filelog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, Filelog)

# Python 3 usa C3 suplerclass linearization
# para gerar o mro.

# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__(Dunder - Double Underscore)

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    def quem_sou(self):
        print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C):
    ...

    def quem_sou(self):
        print('D')

d = D()
d.quem_sou()

print(D.mro())