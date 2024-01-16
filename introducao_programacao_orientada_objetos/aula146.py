# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exeções
# Adicionando notas em exceções

class MeuError(Exception):
    ...
class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    raise exception_
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error