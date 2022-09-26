nome = "Uéslei"
idade = 28
profissao = "Programador"
linguagem = "Python"

 
dados = {"nome": "Uéslei", "idade": 29}
print("Nome: {nome}, Idade{idade}".format(**dados))

print("Nome: %s | Idade: %d | Profissao: %s | Linguagem: %s" % (nome, idade, profissao, linguagem))
print(f"Nome: {nome} | Idade: {idade} | Profissao: {profissao} | Linguagem: {linguagem}")
print("Nome: {} | Idade: {} | Profissao: {} | Linguagem: {}".format(nome, idade, profissao, linguagem))
#print("Nome: {} | Idade: {} | Profissao: {} | Linguagem: {}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Nome: {1} | Idade: {0} | Profissao: {2} | Linguagem: {3}, {2} {2}".format(idade, nome, profissao, linguagem))


valor = 24.4526

print(f'O valor é {valor:.2f}')
print(f'O valor é {valor:10.2f}') # adiciona espaços antes.