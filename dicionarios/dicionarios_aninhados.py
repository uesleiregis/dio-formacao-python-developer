# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "vanessa_123@gmail.com": {"nome": "Vanessa", "telefone": "3333-2221"},
#     "thiago_i231@gmail.com": {"nome": "Thiago", "telefone": "3325-2221"},
#     "elene_01e@gmail.com": {"nome": "Elena", "telefone": "3333-2221", "extra": {"a": 1}},

# }

# print(contatos["guilherme@gmail.com"]["telefone"])

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "vanessa_123@gmail.com": {"nome": "Vanessa", "telefone": "3333-2221"},
    "thiago_i231@gmail.com": {"nome": "Thiago", "telefone": "3325-2221"},
    "elene_01e@gmail.com": {"nome": "Elena", "telefone": "3333-2221", "extra": {"a": 1}},

}

telefone = contatos["guilherme@gmail.com"]["telefone"] 
print(telefone)

extra = contatos["elene_01e@gmail.com"]["extra"]["a"]


print(extra)
