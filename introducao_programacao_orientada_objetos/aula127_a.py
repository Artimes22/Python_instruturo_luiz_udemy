# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = '.\\introducao_programacao_orientada_objetos\\aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)        
p2 = Pessoa('Maria', 20)        
p3 = Pessoa('Jessica', 15)        
banco_de_dados = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(banco_de_dados, arquivo, ensure_ascii=False, indent=2)