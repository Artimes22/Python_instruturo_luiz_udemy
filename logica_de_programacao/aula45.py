"""
Interavel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu interador
"""


# texto = iter('Artimes') #__iter__()
# print(texto)
# print(next(texto)) #__next__()

#for letra in texto
texto = 'Artimes' #iterável
iteratador = iter(texto) #iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break