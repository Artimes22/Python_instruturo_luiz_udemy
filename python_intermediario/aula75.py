"""
Exercícios
Crie funções que duplica,, triplicam e quadriplicam
o número recebido como parâmetro.
"""

# def duplica(numero):
#     return numero * 2
# def triplica(numero):
#     return numero * 3
# def quadriplica(numero):
#     return numero * 4

# print(duplica(2))
# print(triplica(2))
# print(quadriplica(2))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))