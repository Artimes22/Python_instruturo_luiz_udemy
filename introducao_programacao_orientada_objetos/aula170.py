# os.listdir para navegar em caminhos
#C:\Users\Usuario\Documents\Artimes\estudos
import os

caminho = os.path.join('/Users','Usuario', 'Documents', 'Artimes', 'estudos')

for item in os.listdir(caminho):
    print(item)