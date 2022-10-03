
class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilerme", 1)
aluno_2 = Estudante("Giovana", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" # Troquei a variável de classe, isto é, troquei para todas as variáveis seguintes. 
aluno_1.matricula = 3 # alterando instância do objeto

aluno_3 = Estudante("Chappie ", 3)

mostrar_valores(aluno_1, aluno_2, aluno_3) 

