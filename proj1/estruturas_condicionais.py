saldo = 2000
for x in range(10):
  
    saque = float(input("Informe o valor do saque: "))

    if saldo >= saque:
        print('Realizando o saque!')
        saldo -= saque
        print(f'Saldo atual: {saldo}')
        
    else:
        print('Saldo insuficiente')
        print(f'Saldo atual: {saldo}')
