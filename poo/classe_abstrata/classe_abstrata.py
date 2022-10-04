
from abc import ABC, abstractmethod # importando do módulo abc a classe ABC

class ControleRemoto(ABC): # controle remoto estende de ABC, herda os métodos da classe ABC
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):

    def ligar(self):
        print('Ligando a TV')
        print('Ligado')
    
    
    def desligar(self):
        print('Desligando a TV')
        print('Desligado')


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado ')
        print('Ligado')
    
    
    # def desligar(self):
    #     print('Desligando o Ar Condicionado')
    #     print('Desligado')

controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()

