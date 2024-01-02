# Encapsulamento (modificadores de acesso: public, protected e private)
# Python NÂO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#     (sem underline) = piblic
#         pode ser usado em qualquer lugar
#  -  (um underline) = protected
#         NÃO DEVE ser usado fora da classe 
#         ou suas subclasses.
#  __ (dois underlines) = private
#         "name mangling" (desfiguração de nomes) em Python
#         só DEVE ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'isso é private'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
        return 'metodo_private'

f = Foo()
print(f.public)
print(f.metodo_publico())  
print()
print(f._protected)
print(f._metodo_protected())     
print()
print(f.__private)
print(f.__metodo_private())