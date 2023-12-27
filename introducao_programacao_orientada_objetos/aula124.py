# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        self.filmando = True
        print(f'{self.nome} está filmando...') 

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÂO está filmando...')
            return
        self.filmando = False
        print(f'{self.nome} está parando de filmar') 
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} NÂO pode fotografar enquanto estiver filmando')
            return            
        self.foto = True
        print(f'{self.nome} tirou uma foto')    
c1 = Camera('Canon')
c2 = Camera('Sony')

# c1.filmar()
# c1.filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
print()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()
print()