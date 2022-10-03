class Conta:
    def __init__(self, nro_agencia, saldo =0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor
        

    def sacar(self, valor):
        self._saldo -= valor

 

# Instanciando o meu objeto
conta = Conta( "001100", 100)
#conta._saldo += 100 # não é recomendado, estou driblando o encapsulamento
conta.depositar(50) # maneira correta, usando método para depositar
print(conta._saldo)
print(conta.nro_agencia) # como não é privado, está tudo bem isso.