# @property - um getter no Pythônico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguites situações:
# - como getter
# - p/ envitar quebrar código cliente
# Código cliente - é o código que usa seu código 
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo 

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123

#############################

caneta = Caneta('Azul')

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)


# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta    
    
# #############################

# caneta = Caneta('Azul')

# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())


