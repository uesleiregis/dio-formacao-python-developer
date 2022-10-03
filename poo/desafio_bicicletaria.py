
# Crie um programa onde João informe: 
# cor, modelo, ano, e valor da bicicleta vendida 
# a bicicleta pode buzinar, parar e correr.
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self): # sempre declarar o self
        print("Buzinou")

    def parar(self):
        print("Parou")

    def correr(self):
        print("Correu")

    # exibindo as nossas instâncias
    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"


# há um erro nas duas linhas seguintes que não consigo identificar. 
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta("vermelha", "caloi", 2020, 700)
caloi.buzinar()
caloi.parar()
caloi.correr()
b = caloi # acesso o mesmo endereço de memória do objeto calooi
b.ano = 2000
print(b.cor, b.modelo, b.ano, b.valor)

print(caloi)
