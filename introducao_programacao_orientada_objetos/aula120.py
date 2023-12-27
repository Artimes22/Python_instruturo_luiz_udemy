# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que 
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de 
# classes
# string = 'Luiz' #str
# print(string.upper())
# print(isinstance(string, str))

class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = pessoa('Maria', 'Joseane')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joseane'



print(p1.nome)    
print(p1.sobrenome)   
 
print(p2.nome)    
print(p2.sobrenome)    