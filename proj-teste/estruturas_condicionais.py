MAIOR_IDADE = 18


idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH')
else: 
    print('Não pode tirar a CNH')

saldo = 100
saque = 150

status = "Sucesso" if saldo >= saque else "Falha"

print(f'{status} ao realizar o saque!')