# setdefault

# se o atributo não estiver no dicionário, ele adiciona com o atributo que eu adicionei aqui. 

# se o atributo já existir, ele retorna o valor que está no dicionário e não altera ele. 

contato = {'nome': 'Uéslei', 'telefone': '3332-1234'}

print(contato)

print(  contato.setdefault('nome', 'Giovana')  )
print( contato )

print(  contato.setdefault('idade', 28)  )
print( contato )