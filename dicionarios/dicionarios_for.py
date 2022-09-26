# iterando em dicionarios com python

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "vanessa_123@gmail.com": {"nome": "Vanessa", "telefone": "3333-2221"},
    "thiago_i231@gmail.com": {"nome": "Thiago", "telefone": "3325-2221"},
    "elene_01e@gmail.com": {"nome": "Elena", "telefone": "3333-2221", "extra": {"a": 1}},

}

# essa não é a melhor
for chave in contatos:
    print(chave, contatos[chave])

# items retorna uma lista de tuplas pra nós.
# for chave, valor in contatos.items():
#     print(chave, valor)