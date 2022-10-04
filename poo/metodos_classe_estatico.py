# Aprendendo a utilizar Métodos de Estáticos




class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    # Método de fábrica
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022- ano
        print(cls)
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa('Uéslei', 19)
# print(p.nome, p.idade)

# p2 = Pessoa().criar_de_data_nascimento(1994, 3,21, 'Uéslei' )
# print(p2.nome, p2.idade)

p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Uéslei")

print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(12))



