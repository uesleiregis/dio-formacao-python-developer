
class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
            print("Objeto destruido. Removendo a instancia da classe")
        
    def falar(self):
        print("au au")
 
    def criar_cachorro(self):
        c = Cachorro("Zeus", "Branco e preto", False)
        print(c.nome)
   


c = Cachorro("Chappie", "Amarelo")
# c.falar()


c.criar_cachorro()