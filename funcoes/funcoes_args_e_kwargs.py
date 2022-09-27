# pessoa = {"nome": "Guilherme", "idade": 28}
# print(pessoa.items()) # revisando ... retorna lista de itens do dicionário (chave e valor)

# exemplo do uso de Args e kwargs

def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de Agosto de 2022","Zen of Python",
    "Beautiful is better than ugly.",
    "Continuando o teste",
    autor="Tim Peters", ano = 1999)