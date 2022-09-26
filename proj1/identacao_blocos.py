def sacar(valor):
    saldo =500

    if saldo >= valor:
        print("""
        Perfeito!!!
        Pode retirar o seu dinheiro.
        """)

print("Obrigado por usar os nosso serviços")

def depositar(valor):
    saldo = 500
    saldo += valor

depositar(100)
sacar(100)