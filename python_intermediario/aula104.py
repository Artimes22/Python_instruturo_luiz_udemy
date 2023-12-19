# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
            resltado = func(*args, **kwargs)
            print(f'O seu resultado foi {resltado}.')
            print('Ok, agora você foi decorada')
        return resltado
    return interna

@criar_funcao #Syntax Sugar
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
invertida = inverte_string('123')
print(invertida)   