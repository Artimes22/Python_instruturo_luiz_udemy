# Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escrever ao final), b (binario)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (mover o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo 
# os.rename - troca o nome ou move o arquivo
# Vamos falar mnais sobre o módulo json, mas:
# json.dump = Gera um arquivo json 
# json.load 

caminho_arquivo = 'C:\\Users\\Usuario\\Documents\\Artimes\\nova pasta projeto\\'
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
# 'w' sempre vai apagar o que estava salvo sempre que abrir o arquivo novamente
# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

# print('#' * 10)    

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

#=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=

# 'a' vai pegar o arquivo salvo e continuar sem alterar o que ja estava salvo
# with open(caminho_arquivo, 'a') as arquivo:

#     arquivo.write('"a" append\n')
#     arquivo.write('Linha 5\n')
#     arquivo.write('Linha 6\n')
#     arquivo.writelines(
#         ('Linha 7\n', 'Linha 8\n')
#     )

#=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=

with open(caminho_arquivo, 'w', encoding= 'utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
