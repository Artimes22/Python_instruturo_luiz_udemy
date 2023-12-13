#  Modularização - Entendendo os seus próprios módulos Python
#  O Primeiro módulo executado chama-se __main__
#  Você pode importar outro módulo interno ou parte do módulo
#  O Python conhece a pasta onde o __main__ está e as pastas
#  abaixo dele.
#  Ele não reconhece pastas e módulos acima do __mian__ por
#  padrão
#  O python conhece todos os módulos e pacotes presentes 
#  nos caminhos de sys.path
import aula97_m

print('Este módulo se chama', __name__)
print(aula97_m.variavel_nome)
print(aula97_m.soma(8, 2))