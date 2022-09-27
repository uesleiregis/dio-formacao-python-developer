


deposito = 0
saldo = 0

def depositar():
    deposito = int(input('Informe o valor para Depósito: '))
    if deposito <=0:
        deposito = int(input('Informe outro valor para depósto: '))
    return deposito


MAX_SAQUES = 3

def sacar(saque):
    saque = int(input('Quanto deseja sacar? '))
    if saldo == 0:
        print('Não é possível sacar por falta de saldo.')
    elif saque <= saldo:
        saque = int(input('Saldo insuficiente. Informe um valor diferente pra saque: R$ '))
    else: 
        


def extrato()