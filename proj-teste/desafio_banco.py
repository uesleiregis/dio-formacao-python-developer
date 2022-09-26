

SALDO_INICIAL = int(input('Informe o saldo inicial: '))

saldo = SALDO_INICIAL
saques = []
depositos = []

def deposito(saldo=saldo):
    v = 0
    while(v <= 0 ):
        v = int(input('Informe um valor para depósito: '))

    saldo += v
    depositos.append(v)
    print(f'R${v} depositado com sucesso!')
    print(f'Saldo atual R$ {saldo}.\n')
   

def saque(saldo=saldo):
    valor = 0

    while(valor <= 0 or valor > 500):
        valor = int(input('Informe um valor para saque: '))
        if valor <= 0 or valor > 500:
            print(f'{valor} é uma quantia inválida.')

    saldo -= valor
    saques.append(valor)
    print(f'R${valor} sacado com sucesso!')
    print(f'Saldo atual R$ {saldo}.\n')
   
def extrato():
    print(f'Saques efetuados {saques}\n')
    print(f'Depósitos Efetuados {depositos}\n')
    print(f'O saldo atual é {saldo}\n')



while(True):
    op = int(input(f'''----------------------------------
    Que operação gostaria de fazer?
    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair
    ----------------------------------
    '''))

    if (op == 1):
        deposito()
    elif(op == 2):
        saque()
    elif(op == 3):
        saque()
    elif(op == 0):
        break
