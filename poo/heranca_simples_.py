class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado == True else 'Sim'} estou carregado")

    def __str__(self):
        return f"{self.__class__.__nome__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

moto = Motocicleta('branca', 'mve-2443', 2)
carro = Carro('branco', 'xde-0495', 4)
caminhao = Caminhao('roxa', 'gfd-8712', 6, True)

print(moto)
print(carro)
print(caminhao)